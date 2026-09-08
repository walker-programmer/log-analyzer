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

            log_entry = parse_line(line)
            analyzer.process(log_entry)

    return analyzer


def main():
    parser = argparse.ArgumentParser(description="Analyze web server access logs.")
    parser.add_argument("logfile", help="Path to the access log file")

    args = parser.parse_args()

    try:
        analyzer = analyze_file(args.logfile)
    except FileNotFoundError:
        print(f"Error: file not found: {args.logfile}")
        return

    print(f"Total requests: {analyzer.total_requests}")
    print(f"Total response size: {analyzer.total_response_size}")
    print(f"Methods: {analyzer.methods}")
    print(f"Status codes: {analyzer.status_codes}")
    print(f"URLs: {analyzer.urls}")
    print(f"IPs: {analyzer.ips}")


if __name__ == "__main__":
    main()
