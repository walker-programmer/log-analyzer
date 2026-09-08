import pytest

from log_analyzer.__main__ import analyze_file, format_report
from log_analyzer.analyzer import Analyzer


def test_analyze_file(tmp_path):
    log_file = tmp_path / "test.log"

    log_file.write_text(
        "192.168.1.10 - - [30/Aug/2026:10:15:32 +0300] "
        '"GET /index.html HTTP/1.1" 200 1543\n'
        "192.168.1.11 - - [30/Aug/2026:10:17:05 +0300] "
        '"POST /login HTTP/1.1" 302 512\n',
        encoding="utf-8",
    )

    analyzer = analyze_file(str(log_file))

    assert analyzer.total_requests == 2
    assert analyzer.total_response_size == 2055
    assert analyzer.methods == {"GET": 1, "POST": 1}
    assert analyzer.status_codes == {200: 1, 302: 1}


def test_analyze_file_file_not_found():
    with pytest.raises(FileNotFoundError):
        analyze_file("nonexistent.log")


def test_analyze_file_skips_invalid_line(tmp_path):
    log_file = tmp_path / "test.log"

    log_file.write_text(
        "invalid log line\n"
        "192.168.1.10 - - [30/Aug/2026:10:15:32 +0300] "
        '"GET /index.html HTTP/1.1" 200 1543\n',
        encoding="utf-8",
    )

    analyzer = analyze_file(str(log_file))

    assert analyzer.total_requests == 1
    assert analyzer.total_response_size == 1543


def test_format_report():
    analyzer = Analyzer()

    analyzer.total_requests = 2
    analyzer.total_response_size = 2055
    analyzer.methods = {"GET": 1, "POST": 1}
    analyzer.status_codes = {200: 1, 302: 1}
    analyzer.urls = {"/index.html": 1, "/login": 1}
    analyzer.ips = {"192.168.1.10": 1, "192.168.1.11": 1}

    report = format_report(analyzer)

    assert "Log Analysis Report" in report
    assert "Total requests: 2" in report
    assert "Total response size: 2055 bytes" in report

    assert "Methods:" in report
    assert "  GET: 1" in report
    assert "  POST: 1" in report

    assert "Status codes:" in report
    assert "  200: 1" in report
    assert "  302: 1" in report

    assert "URLs:" in report
    assert "  /index.html: 1" in report
    assert "  /login: 1" in report

    assert "IPs:" in report
    assert "  192.168.1.10: 1" in report
    assert "  192.168.1.11: 1" in report
