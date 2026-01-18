# src/video_input/video_input.py
import cv2

class VideoInput:
    def __init__(self, source):
        self.cap = cv2.VideoCapture(source)

    def get_frame(self):
        ret, frame = self.cap.read()
        return frame if ret else None

    def release(self):
        self.cap.release()
