import unittest
import cv2
from src.detection.vehicle_accident_detector import VehicleAccidentDetector


class TestVehicleAccidentDetector(unittest.TestCase):
    def test_detect(self):

        cap = cv2.VideoCapture('test_videos/sample.mp4')
        ret, frame = cap.read()
        cap.release()

        self.assertTrue(ret, "Failed to read frame from video")

        detector = VehicleAccidentDetector(threshold=0.01)
        detected, metadata = detector.detect(frame)

        self.assertIsInstance(detected, bool)
        if detected:
            self.assertIn('timestamp', metadata)
            self.assertIn('confidence', metadata)


if __name__ == "__main__":
    unittest.main()
