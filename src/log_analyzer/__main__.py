import argparse

from .analyzer import Analyzer
from .parser import parse_line


def analyze_file(filename: str) -> Analyzer:
    analyzer = Analyzer()

    with open(filename, encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            try:
                log_entry = parse_line(line)
            except ValueError:
                print("Warning: invalid log line, skipped")
                continue

            analyzer.process(log_entry)

    return analyzer


def format_report(analyzer: Analyzer) -> str:
    lines = [
        "Log Analysis Report",
        "-------------------",
        f"Total requests: {analyzer.total_requests}",
        f"Total response size: {analyzer.total_response_size} bytes",
        "",
        "Methods:",
    ]

    for method, count in analyzer.methods.items():
        lines.append(f"  {method}: {count}")

    lines.append("")
    lines.append("Status codes:")

    for status_code, count in analyzer.status_codes.items():
        lines.append(f"  {status_code}: {count}")

    lines.append("")
    lines.append("URLs:")

    for url, count in analyzer.urls.items():
        lines.append(f"  {url}: {count}")

    lines.append("")
    lines.append("IPs:")

    for ip, count in analyzer.ips.items():
        lines.append(f"  {ip}: {count}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Analyze web server access logs.")
    parser.add_argument("logfile", help="Path to the access log file")

    args = parser.parse_args()

    try:
        analyzer = analyze_file(args.logfile)
    except FileNotFoundError:
        print(f"Error: file not found: {args.logfile}")
        return

    print(format_report(analyzer))


if __name__ == "__main__":
    main()
