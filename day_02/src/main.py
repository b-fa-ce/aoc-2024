from utils import (
    read_file,
    is_safe_report,
    is_safe_report_with_dampener,
    count_safe_reports,
)

if __name__ == "__main__":
    reports = read_file("data.csv")

    safe_reports = count_safe_reports(reports, is_safe_report)
    safe_report_with_dampener = count_safe_reports(
        reports, is_safe_report_with_dampener
    )

    print(
        f"""
          safe reports: {safe_reports}
          safe reports with dampener: {safe_report_with_dampener}"""
    )
