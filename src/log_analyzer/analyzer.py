from .models import LogEntry


class Analyzer:
    def __init__(self):
        self.total_requests = 0
        self.methods = {}
        self.status_codes = {}
        self.urls = {}
        self.ips = {}
        self.total_response_size = 0

    def process(self, log_entry: LogEntry):
        self.total_requests += 1

        if log_entry.ip in self.ips:
            self.ips[log_entry.ip] += 1
        else:
            self.ips[log_entry.ip] = 1

        if log_entry.method in self.methods:
            self.methods[log_entry.method] += 1
        else:
            self.methods[log_entry.method] = 1

        if log_entry.status_code in self.status_codes:
            self.status_codes[log_entry.status_code] += 1
        else:
            self.status_codes[log_entry.status_code] = 1

        if log_entry.url in self.urls:
            self.urls[log_entry.url] += 1
        else:
            self.urls[log_entry.url] = 1

        self.total_response_size += log_entry.response_size
