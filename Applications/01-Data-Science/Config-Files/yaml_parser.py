"""
Comprehensive example: Loading YAML config files into Python dataclasses.

Covers:
  - Basic dataclass with type hints
  - Nested dataclasses
  - Optional fields and defaults
  - Lists and dicts of sub-configs
  - Post-init validation
  - Custom deserialization (e.g. enums, paths)
  - A reusable generic loader
  - Merging a base config with environment overrides

Requirements:
    pip install pyyaml dacite
    (dacite handles recursive dataclass construction from dicts)
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional

import yaml
from dacite import Config as DaciteConfig
from dacite import from_dict


# ---------------------------------------------------------------------------
# Enums used in config
# ---------------------------------------------------------------------------


class LogLevel(str, Enum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"


class Environment(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"


# ---------------------------------------------------------------------------
# Dataclass hierarchy
# ---------------------------------------------------------------------------


@dataclass
class DatabaseConfig:
    host: str
    port: int
    name: str
    user: str
    password: str
    pool_size: int = 5
    ssl: bool = False

    def __post_init__(self) -> None:
        if not 1 <= self.port <= 65535:
            raise ValueError(f"Invalid port number: {self.port}")
        if self.pool_size < 1:
            raise ValueError("pool_size must be at least 1")

    @property
    def url(self) -> str:
        scheme = "postgresql+psycopg2"
        return f"{scheme}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


@dataclass
class CacheConfig:
    host: str
    port: int = 6379
    ttl_seconds: int = 300
    max_connections: int = 10


@dataclass
class ServiceEndpoint:
    url: str
    timeout_seconds: float = 5.0
    retries: int = 3
    api_key: Optional[str] = None


@dataclass
class FeatureFlags:
    enable_new_ui: bool = False
    enable_beta_api: bool = False
    max_upload_mb: int = 10
    allowed_origins: list[str] = field(default_factory=list)


@dataclass
class LoggingConfig:
    level: LogLevel = LogLevel.INFO
    json_output: bool = False
    log_dir: Optional[Path] = None

    def __post_init__(self) -> None:
        # Ensure log_dir exists if specified
        if self.log_dir is not None:
            self.log_dir = Path(self.log_dir)
            self.log_dir.mkdir(parents=True, exist_ok=True)


@dataclass
class AppConfig:
    """Root configuration object."""

    app_name: str
    environment: Environment
    version: str
    database: DatabaseConfig
    logging: LoggingConfig
    cache: Optional[CacheConfig] = None
    feature_flags: FeatureFlags = field(default_factory=FeatureFlags)
    # Named external services, e.g. services.payment, services.email
    services: dict[str, ServiceEndpoint] = field(default_factory=dict)
    debug: bool = False

    def __post_init__(self) -> None:
        if self.environment == Environment.PRODUCTION and self.debug:
            raise ValueError("debug must be False in production")


# ---------------------------------------------------------------------------
# Generic YAML → dataclass loader
# ---------------------------------------------------------------------------


def _load_yaml(path: str | Path) -> dict:
    """Read a YAML file and return its contents as a plain dict."""
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def _deep_merge(base: dict, override: dict) -> dict:
    """
    Recursively merge *override* into *base*.
    Override values win; nested dicts are merged rather than replaced.
    """
    result = dict(base)
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def load_config(
    config_path: str | Path,
    override_path: Optional[str | Path] = None,
    env_prefix: str = "APP_",
) -> AppConfig:
    """
    Build an AppConfig from:
      1. A base YAML file
      2. An optional environment-specific override YAML file
      3. Environment variables (APP_DATABASE__HOST, etc.)

    Env-var override format:
        APP_<SECTION>__<KEY>=value   (double underscore = nesting level)
    e.g. APP_DATABASE__HOST=db.prod.internal
    """

    data = _load_yaml(config_path)

    if override_path and Path(override_path).exists():
        overrides = _load_yaml(override_path)
        data = _deep_merge(data, overrides)

    # Apply environment variable overrides
    data = _apply_env_overrides(data, env_prefix)

    return from_dict(
        data_class=AppConfig,
        data=data,
        config=DaciteConfig(
            cast=[Enum, Path],          # auto-cast str → Enum / Path
            strict=False,               # ignore unknown keys gracefully
        ),
    )


def _apply_env_overrides(data: dict, prefix: str) -> dict:
    """
    Walk environment variables that start with *prefix* and apply them to
    the config dict using double-underscore as a path separator.

    Example:
        APP_DATABASE__PORT=5433  →  data["database"]["port"] = "5433"
    """

    for key, value in os.environ.items():
        if not key.startswith(prefix):
            continue
        path_str = key[len(prefix):].lower()  # e.g. "database__port"
        parts = path_str.split("__")          # ["database", "port"]
        node = data
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        # Attempt simple type coercion
        node[parts[-1]] = _coerce(value)
    return data


def _coerce(value: str):
    """Best-effort coercion of env-var strings to int / float / bool."""
    if value.lower() in ("true", "yes", "1"):
        return True
    if value.lower() in ("false", "no", "0"):
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

def demo_from_string() -> None:
    """Parse configs from in-memory strings (no files required)."""

    with open('base_config.yaml', 'r') as f:
        base_data = yaml.safe_load(f)

    with open('ovrd_config.yaml', 'r') as f:
        override_data = yaml.safe_load(f)

    merged = _deep_merge(base_data, override_data)

    cfg = from_dict(
        data_class=AppConfig,
        data=merged,
        config=DaciteConfig(cast=[Enum, Path], strict=False),
    )

    print("=== AppConfig ===")
    print(f"  app_name    : {cfg.app_name}")
    print(f"  environment : {cfg.environment}")
    print(f"  version     : {cfg.version}")
    print(f"  debug       : {cfg.debug}")

    print("\n=== Database ===")
    print(f"  url         : {cfg.database.url}")
    print(f"  pool_size   : {cfg.database.pool_size}")
    print(f"  ssl         : {cfg.database.ssl}")

    print("\n=== Cache ===")
    if cfg.cache:
        print(f"  {cfg.cache.host}:{cfg.cache.port}  ttl={cfg.cache.ttl_seconds}s")
    else:
        print("  (not configured)")

    print("\n=== Logging ===")
    print(f"  level       : {cfg.logging.level.value}")
    print(f"  json_output : {cfg.logging.json_output}")

    print("\n=== Feature Flags ===")
    print(f"  new_ui      : {cfg.feature_flags.enable_new_ui}")
    print(f"  beta_api    : {cfg.feature_flags.enable_beta_api}")
    print(f"  max_upload  : {cfg.feature_flags.max_upload_mb} MB")
    print(f"  origins     : {cfg.feature_flags.allowed_origins}")

    print("\n=== External Services ===")
    for name, svc in cfg.services.items():
        print(f"  [{name}] {svc.url}  timeout={svc.timeout_seconds}s")


if __name__ == "__main__":
    base_path = Path('base_config.yaml')
    override_path = Path('ovrd_config.yaml')

    # Simulate an env-var override
    os.environ["APP_DATABASE__PASSWORD"] = "super_secret_from_env"

    cfg = load_config(base_path, override_path, env_prefix="APP_")

    print("=== AppConfig ===")
    print(f"  app_name    : {cfg.app_name}")
    print(f"  environment : {cfg.environment}")
    print(f"  version     : {cfg.version}")
    print(f"  debug       : {cfg.debug}")

    print("\n=== Database ===")
    print(f"  url         : {cfg.database.url}")
    print(f"  pool_size   : {cfg.database.pool_size}")
    print(f"  ssl         : {cfg.database.ssl}")
    print(f"  password    : {cfg.database.password}")

    print("\n=== Cache ===")
    if cfg.cache:
        print(f"  {cfg.cache.host}:{cfg.cache.port}  ttl={cfg.cache.ttl_seconds}s")
    else:
        print("  (not configured)")

    print("\n=== Logging ===")
    print(f"  level       : {cfg.logging.level.value}")
    print(f"  json_output : {cfg.logging.json_output}")

    print("\n=== Feature Flags ===")
    print(f"  new_ui      : {cfg.feature_flags.enable_new_ui}")
    print(f"  beta_api    : {cfg.feature_flags.enable_beta_api}")
    print(f"  max_upload  : {cfg.feature_flags.max_upload_mb} MB")
    print(f"  origins     : {cfg.feature_flags.allowed_origins}")

    print("\n=== External Services ===")
    for name, svc in cfg.services.items():
        print(f"  [{name}] {svc.url}  timeout={svc.timeout_seconds}s")

    print('')
