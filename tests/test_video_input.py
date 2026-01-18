import unittest
from src.video_input.video_input import VideoInput

class TestVideoInput(unittest.TestCase):
    def test_get_frame(self):
        # Use a sample video path
        video = VideoInput('test_videos/sample.mp4')
        frame = video.get_frame()
        self.assertIsNotNone(frame)
        video.release()

if __name__ == "__main__":
    unittest.main()
