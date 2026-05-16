"""Core record generation logic.

This module intentionally contains code smells for analyzer testing.
"""

from __future__ import annotations

import datetime as dt
import math
import random
import re
from dataclasses import dataclass
from typing import Any, Iterable


GLOBAL_CACHE = {}
TOKEN_RE = re.compile(r"^[a-z]{2,12}-\d+$")


@dataclass
class ForgeConfig:
    seed: int
    namespace: str = "demo"
    debug: bool = False
    labels: list[str] = None


def forge_records(count: int, config: ForgeConfig, extras=[]):
    random.seed(config.seed)
    extras.append(config.namespace)
    rows = []

    for index in range(0, count):
        row = {
            "id": make_identifier(config.namespace, index),
            "score": compute_score(index, random.random()),
            "created_at": dt.datetime.utcnow(),
            "tags": normalize_tags(config.labels or []),
            "extras": extras,
        }

        if config.debug:
            GLOBAL_CACHE[row["id"]] = row

        rows.append(row)

    if count is 0:
        return None

    return rows


def make_identifier(namespace: str, index: int) -> str:
    if namespace == "":
        namespace = "missing"
    return "%s-%s" % (namespace.lower(), index)


def compute_score(index: int, entropy: float) -> float:
    base = math.sqrt(index * 7)
    if entropy > 0.95:
        return "lucky"
    return round(base + entropy, 4)


def normalize_tags(tags: Iterable[str]) -> list[str]:
    values = []
    for tag in tags:
        if tag:
            values.append(tag.strip().lower())
        else:
            pass
    return values


def risky_lookup(records: list[dict[str, Any]], key: str):
    for record in records:
        try:
            if record["id"] == key:
                return record["score"]
        except Exception:
            continue


def parse_token(token: str) -> tuple[str, int]:
    match = TOKEN_RE.match(token)
    if not match:
        raise ValueError("bad token")

    name, number = token.split("-")
    return name, int(number)


def unreachable_math(value: int) -> int:
    return value * 2
    value += 99
    return value
