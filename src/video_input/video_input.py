import cv2
import os

class VideoInput:

    def __init__(self, source=None, use_webcam=False):

        self.cap = None

        if source and os.path.isfile(source):
            self.cap = cv2.VideoCapture(source)
            print(f"[VideoInput] Using local video: {source}")

        elif use_webcam:
            self.cap = cv2.VideoCapture(0)
            print("[VideoInput] Using webcam")

        else:
            raise ValueError("No video source provided and webcam not enabled")

        if not self.cap.isOpened():
            raise RuntimeError("Cannot open video source")

    def get_frame(self):
        if self.cap is None or not self.cap.isOpened():
            return None

        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def release(self):
        if self.cap:
            self.cap.release()
            self.cap = None
