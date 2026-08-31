from .models import LogEntry
from datetime import datetime

import re

def parse_line(line: str) -> LogEntry:
    #line = '192.168.1.10 - - [30/Aug/2026:10:15:32 +0300] "GET /index.html HTTP/1.1" 200 1543'
    # Регулярное выражение, разделяющее строку на отдельные логические элементы
    pattern = r'^(\S+) (\S+) (\S+) \[(.*?)\] "([A-Z]+) (\S+) (\S+)" (\d+) (\d+)'
    
    match = re.search(pattern, line)
    
    str_format = "%d/%b/%Y:%H:%M:%S %z"
    
    if not match:
        raise ValueError("Error log line")

    entry = LogEntry(
        ip=match.group(1),
        timestamp=datetime.strptime(match.group(4), str_format),
        method=match.group(5),
        url=match.group(6),
        status_code=int(match.group(8)),
        response_size=int(match.group(9)),
    )

    return entry
    