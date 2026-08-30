"""Command-line entry point for the toy city simulation."""

import argparse

from tycoon import __version__, buildings
from tycoon.city import City


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tycoon-city", description="Run a toy city.")
    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument("--name", default="Toyville", help="city name")
    parser.add_argument("--treasury", type=int, default=1000, help="starting treasury")
    parser.add_argument(
        "--build",
        action="append",
        default=[],
        metavar="BUILDING",
        help=f"place a building (one of: {', '.join(buildings.names())})",
    )
    parser.add_argument("--turns", type=int, default=3, help="turns to simulate")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    city = City(name=args.name, treasury=args.treasury)

    for name in args.build:
        try:
            city.build(name)
        except ValueError as exc:
            print(f"skip {name}: {exc}")

    for _ in range(args.turns):
        delta = city.advance()
        print(f"turn {city.turn}: treasury {city.economy.treasury} ({delta:+d})")

    from tycoon.report import render_summary
    for line in render_summary(city.summary()):
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
