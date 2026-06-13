import subprocess
import sys
import unittest
from datetime import date
from pathlib import Path

from julian_day import get_julian_day, parse_date


REPO_ROOT = Path(__file__).resolve().parent


class JulianDayTests(unittest.TestCase):
    def test_returns_known_julian_day_numbers(self):
        self.assertEqual(get_julian_day(date(2000, 1, 1)), 2451545)
        self.assertEqual(get_julian_day(date(1970, 1, 1)), 2440588)
        self.assertEqual(get_julian_day(date(2024, 2, 29)), 2460370)

    def test_parses_iso_date(self):
        self.assertEqual(parse_date("2026-06-13"), date(2026, 6, 13))

    def test_cli_outputs_julian_day(self):
        completed = subprocess.run(
            [sys.executable, str(REPO_ROOT / "julian_day.py"), "1985-02-17"],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(completed.stdout.strip(), "2446114")

    def test_cli_rejects_invalid_dates(self):
        completed = subprocess.run(
            [sys.executable, str(REPO_ROOT / "julian_day.py"), "2024-02-30"],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("Use YYYY-MM-DD", completed.stderr)


if __name__ == "__main__":
    unittest.main()
