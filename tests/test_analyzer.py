from log_analyzer.analyzer import Analyzer
from log_analyzer.parser import parse_line


def test_count_requests():
    analyzer = Analyzer()

    line = '192.168.1.10 - - [30/Aug/2026:10:15:32 +0300] "GET /index.html HTTP/1.1" 200 1543'
    entry = parse_line(line)
    analyzer.process(entry)

    line = '192.168.1.10 - - [30/Aug/2026:10:15:32 +0300] "GET /index.html HTTP/1.1" 200 1543'
    entry = parse_line(line)
    analyzer.process(entry)

    line = '192.168.1.11 - - [30/Aug/2026:10:15:32 +0300] "GET /index.html HTTP/1.1" 200 1543'
    entry = parse_line(line)
    analyzer.process(entry)

    line = '192.168.1.11 - - [30/Aug/2026:10:15:32 +0300] "POST /index.html HTTP/1.1" 200 1543'
    entry = parse_line(line)
    analyzer.process(entry)

    assert analyzer.total_requests == 4
    assert analyzer.ips["192.168.1.10"] == 2
    assert analyzer.ips["192.168.1.11"] == 2
    assert analyzer.methods["GET"] == 3
    assert analyzer.methods["POST"] == 1
    assert analyzer.status_codes[200] == 4
    assert analyzer.urls["/index.html"] == 4
    assert analyzer.total_response_size == 1543 * 4
