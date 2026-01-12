import unittest
from src.video_input import VideoInput

class TestVideoInput(unittest.TestCase):

    def test_video_file_opens(self):

        video = VideoInput("test/sample/1.mp4")
        self.assertTrue(video.is_opened())

    def test_webcam_opens(self):

        video = VideoInput(0)
        self.assertTrue(video.is_opened())

    def test_can_read_frame(self):

        video = VideoInput("test/sample/1.mp4")
        frame = video.read_frame()
        self.assertIsNotNone(frame)
        self.assertEqual(len(frame.shape), 3)

if __name__ == '__main__':
    unittest.main()
