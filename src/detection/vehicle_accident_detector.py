import cv2
import numpy as np
from datetime import datetime

class VehicleAccidentDetector:
    def __init__(self, threshold=25):
        self.prev_gray = None
        self.threshold = threshold

    def detect(self, frame):

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if self.prev_gray is None:
            self.prev_gray = gray
            return False, None

        flow = cv2.calcOpticalFlowFarneback(
            self.prev_gray, gray, None,
            0.5, 3, 15, 3, 5, 1.2, 0
        )


        mag, _ = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        self.prev_gray = gray

        if np.mean(mag) > self.threshold:
            metadata = {
                "timestamp": datetime.now().isoformat(),
                "confidence": float(np.mean(mag))
            }
            return True, metadata

        return False, None
