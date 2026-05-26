# Python Config Files

Configuration files let programs change behavior without changing source code.
This lesson focuses on YAML-based configuration, structured parsing, and
override files.

## Lessons

1. [YAML Config File Parsing](01_yaml_parser.ipynb)

## Supporting Files

- [base_config.yaml](base_config.yaml) - default configuration values.
- [ovrd_config.yaml](ovrd_config.yaml) - override values layered on top of the
  base config.

## Topics

- Loading YAML data
- Using enums and dataclasses for structured config
- Merging base and override settings
- Validating loaded configuration before using it
