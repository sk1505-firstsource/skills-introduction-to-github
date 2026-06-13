from __future__ import annotations

import argparse
from datetime import date, datetime

JULIAN_DAY_OFFSET = 1721425


def parse_date(value: str) -> date:
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            f"invalid date '{value}'. Use YYYY-MM-DD."
        ) from exc


def get_julian_day(value: date) -> int:
    return value.toordinal() + JULIAN_DAY_OFFSET


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Get the Julian Day Number for a given date."
    )
    parser.add_argument("date", type=parse_date, help="Date in YYYY-MM-DD format")
    args = parser.parse_args()
    print(get_julian_day(args.date))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
