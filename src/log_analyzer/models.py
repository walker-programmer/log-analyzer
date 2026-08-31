from dataclasses import dataclass
from datetime import datetime


@dataclass
class LogEntry:
    ip: str
    timestamp: datetime
    method: str
    url: str
    status_code: int
    response_size: int