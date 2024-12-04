from aoc_2024.day_02.src.utils import (
    read_file,
    is_safe_report,
    is_safe_report_with_dampener,
    count_safe_reports,
)


def main():
    reports = read_file("aoc_2024/day_02/data.csv")

    safe_reports = count_safe_reports(reports, is_safe_report)
    safe_report_with_dampener = count_safe_reports(
        reports, is_safe_report_with_dampener
    )

    print(
        f"""
            safe reports: {safe_reports}
            safe reports with dampener: {safe_report_with_dampener}
            """
    )


if __name__ == "__main__":
    main()
