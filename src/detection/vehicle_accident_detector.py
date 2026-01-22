import cv2
import numpy as np
from datetime import datetime, timedelta

class VehicleAccidentDetector:
    def __init__(
        self,
        threshold,
        min_consecutive_frames,
        cooldown_seconds
    ):
        self.threshold = threshold
        self.min_consecutive_frames = min_consecutive_frames
        self.cooldown_seconds = cooldown_seconds

        self.prev_gray = None
        self.motion_counter = 0
        self.last_alert_time = None

    def detect(self, frame):
        gray = self._to_gray(frame)

        if self.prev_gray is None:
            self.prev_gray = gray
            self.motion_counter = 0
            return False, None

        motion_score = self._compute_motion(self.prev_gray, gray)

    #    print(
     #       f"[DEBUG] motion_score={motion_score:.4f}, "
      #      f"counter={self.motion_counter}, "
       #     f"threshold={self.threshold}"
       # )

        self.prev_gray = gray

        if motion_score > self.threshold:
            self.motion_counter += 1
        else:
            self.motion_counter = 0

     #   if motion_score > self.threshold:
      #      print("🚨 motion_score high, checking alert conditions...")

        if self._should_trigger_alert():
            self.last_alert_time = datetime.now()
            self.motion_counter = 0
            return True, self._build_metadata(motion_score)

        return False, None

    def _to_gray(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    def _compute_motion(self, prev_gray, gray):
        h, w = gray.shape
        prev_gray = prev_gray
        gray = gray

        flow = cv2.calcOpticalFlowFarneback(
            prev_gray, gray, None,
            0.5, 3, 15, 3, 5, 1.2, 0
        )

        mag, _ = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        return float(np.mean(mag))

    def _should_trigger_alert(self):
        if self.motion_counter < self.min_consecutive_frames:
            return False

        if self.last_alert_time is None:
            return True

        return datetime.now() - self.last_alert_time > timedelta(
            seconds=self.cooldown_seconds
        )

    def _build_metadata(self, confidence):
        return {
            "timestamp": datetime.now().isoformat(),
            "confidence": confidence
        }
