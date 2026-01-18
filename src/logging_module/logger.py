import json

class EventLogger:
    def __init__(self, log_file='events.json'):
        self.log_file = log_file

    def log(self, event_name, metadata):
        log_entry = {
            "event": event_name,
            "metadata": metadata
        }
        with open(self.log_file, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
