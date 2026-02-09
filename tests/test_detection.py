import unittest
import cv2
from src.detection.vehicle_accident_detector import VehicleAccidentDetector


class TestVehicleAccidentDetector(unittest.TestCase):

    def setUp(self):
        self.detector = VehicleAccidentDetector(
            threshold=0.01,
            min_consecutive_frames=2,
            cooldown_seconds=1
        )

    def test_detect_returns_bool(self):
        cap = cv2.VideoCapture('test_videos/sample.mp4')
        ret, frame = cap.read()
        cap.release()

        self.assertTrue(ret, "Failed to read frame from video")

        detected, metadata = self.detector.detect(frame)

        self.assertIsInstance(detected, bool)

    def test_metadata_structure_when_detected(self):
        cap = cv2.VideoCapture('test_videos/sample.mp4')

        detected = False
        metadata = None

        for _ in range(10):
            ret, frame = cap.read()
            if not ret:
                break
            detected, metadata = self.detector.detect(frame)
            if detected:
                break

        cap.release()

        if detected:
            self.assertIn('timestamp', metadata)
            self.assertIn('confidence', metadata)
