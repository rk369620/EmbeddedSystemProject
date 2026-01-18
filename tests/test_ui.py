import unittest
from src.ui.interface import MonitorUI


class TestMonitorUI(unittest.TestCase):
    def test_update_status(self):
        ui = MonitorUI()
        self.assertEqual(ui.label.cget("text"), "System Idle")

        ui.update_status("Vehicle Accident Detected!")
        self.assertEqual(ui.label.cget("text"), "Vehicle Accident Detected!")


if __name__ == "__main__":
    unittest.main()
