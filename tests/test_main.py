from log_analyzer.__main__ import analyze_file


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
