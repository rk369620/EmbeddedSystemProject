import unittest
from src.communication.communicator import Communicator


class TestCommunicator(unittest.TestCase):
    def test_send_alert(self):

        # Use dummy IP for local test (will fail until implemented)
        comm = Communicator('127.0.0.1:5000')

        # Attempt to send activate alert
        result = comm.send_alert('activate')
        self.assertIsInstance(result, bool)


if __name__ == "__main__":
    unittest.main()
