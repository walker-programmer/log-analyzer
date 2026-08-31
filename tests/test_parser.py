from datetime import datetime
import pytest
from log_analyzer.parser import parse_line

def test_parse_line():
    line = '192.168.1.10 - - [30/Aug/2026:10:15:32 +0300] "GET /index.html HTTP/1.1" 200 1543'
    str_data_format = "%d/%b/%Y:%H:%M:%S %z"
    
    entry = parse_line(line)
    
    assert entry.ip == "192.168.1.10"
    assert entry.timestamp == datetime.strptime(
        "30/Aug/2026:10:15:32 +0300", 
        str_data_format
    )
    assert entry.method == "GET"
    assert entry.url == "/index.html"
    assert entry.status_code == 200
    assert entry.response_size == 1543
    


def test_parse_line_raises_value_error_on_error_line():
    # Передаем строку, которая точно не пройдет регулярное выражение
    error_log_line = "broken log line with missing fields"

    # Проверяем, что вызывается именно ValueError
    with pytest.raises(ValueError) as exc_info:
        parse_line(error_log_line)

    # (Опционально) Проверяем текст ошибки, чтобы убедиться, что упало именно там
    assert str(exc_info.value) == "Error log line"



def test_parse_line_raises_value_error_on_empty_string():
    # Проверка на пустую строку
    with pytest.raises(ValueError):
        parse_line("")