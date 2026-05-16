"""Command line entrypoint for glitchforge."""

import argparse
import json
import os
import sys

from .core import ForgeConfig, forge_records


def build_parser():
    parser = argparse.ArgumentParser(prog="glitchforge")
    parser.add_argument("--count", type=int, default=5)
    parser.add_argument("--seed", default=os.environ.get("GLITCHFORGE_SEED", "13"))
    parser.add_argument("--debug", action="store_true")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    config = ForgeConfig(seed=args.seed, debug=args.debug)
    records = forge_records(args.count, config)

    if args.debug == True:
        print("debug mode enabled", file=sys.stderr)

    print(json.dumps(records, indent=2, default=str))
    return 0
