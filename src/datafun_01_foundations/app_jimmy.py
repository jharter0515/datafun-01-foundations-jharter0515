"""
app_jimmy.py - Project script.

Author: Jimmy Harter
Date: 2026-01

Practice key Python skills related to:
- imports
- logging
- variables
- type hints
- global constants
- f-strings
- functions
- main function
- conditional execution guard

OBS:
This is your file to practice and customize.
"""

import logging
import statistics
from typing import Final

from datafun_toolkit.logger import get_logger, log_header


# === CONFIGURE LOGGER ===
LOG: logging.Logger = get_logger("P01", level="INFO")


# === DECLARE GLOBAL CONSTANTS ===
COURSE_NAME: Final[str] = "Data Fundamentals"
STUDENT_COUNT: Final[int] = 24
AVERAGE_SCORE: Final[float] = 88.6
COURSE_ACTIVE: Final[bool] = True
TOPICS: Final[list[str]] = ["Python", "Git", "uv", "Foundations"]

# Change one value in the list
TOPICS[3] = "Project Setup"


# === FUNCTION: SUMMARY OF GLOBAL VARIABLES ===
def get_summary() -> str:
    summary = (
        f"Course Name: {COURSE_NAME}\n"
        f"Student Count: {STUDENT_COUNT}\n"
        f"Average Score: {AVERAGE_SCORE}\n"
        f"Course Active: {COURSE_ACTIVE}\n"
        f"Topics Covered: {', '.join(TOPICS)}"
    )
    return summary


# === FUNCTION: DESCRIPTIVE STATISTICS ===
def get_statistics() -> str:
    snowfall_inches = [2.5, 3.5, 4.5, 5.5, 6.5]

    total = sum(snowfall_inches)
    count = len(snowfall_inches)
    average = statistics.mean(snowfall_inches)
    min_snowfall = min(snowfall_inches)
    max_snowfall = max(snowfall_inches)
    stdev_snowfall = statistics.stdev(snowfall_inches)

    summary = (
        "Descriptive Statistics for Snowfall (inches):\n"
        f"Total snowfall: {total:.2f} inches\n"
        f"Count of measurements: {count}\n"
        f"Minimum snowfall: {min_snowfall:.2f} inches\n"
        f"Maximum snowfall: {max_snowfall:.2f} inches\n"
        f"Average snowfall: {average:.2f} inches\n"
        f"Standard deviation: {stdev_snowfall:.2f} inches\n"
    )

    return summary


# === MAIN FUNCTION ===
def main() -> None:
    LOG.info("==============")
    log_header(LOG, "Foundations of Professional Python")
    LOG.info("==============")

    LOG.info("START main()...............")

    summary = get_summary()
    LOG.info(summary)

    stats = get_statistics()
    LOG.info(stats)

    LOG.info("END main()...............")



# === CONDITIONAL EXECUTION GUARD ===
if __name__ == "__main__":
    main()
