import unittest
import os
from src.logging_module.logger import EventLogger

class TestEventLogger(unittest.TestCase):
    def setUp(self):
        self.test_log_file = 'test_events.json'
        if os.path.exists(self.test_log_file):
            os.remove(self.test_log_file)

    def tearDown(self):
        if os.path.exists(self.test_log_file):
            os.remove(self.test_log_file)

    def test_log_event(self):
        logger = EventLogger(self.test_log_file)
        metadata = {"timestamp": "2026-01-18T12:00:00", "confidence": 0.95}
        logger.log("Vehicle Accident", metadata)
        self.assertTrue(os.path.exists(self.test_log_file))

        with open(self.test_log_file, 'r') as f:
            content = f.read()
        self.assertIn("Vehicle Accident", content)
        self.assertIn("0.95", content)

if __name__ == "__main__":
    unittest.main()
