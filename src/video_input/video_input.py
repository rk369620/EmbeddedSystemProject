import cv2
import os
import yt_dlp

class VideoInput:
    def __init__(self, source, fallback_video=None, temp_folder='test_videos'):

        self.temp_folder = temp_folder
        os.makedirs(temp_folder, exist_ok=True)
        self.fallback_video = fallback_video

        if isinstance(source, str) and source.startswith("http"):
            try:
                self.file_path = self.download_video(source)
            except Exception as e:
                print(f"[VideoInput] WARNING: Online video failed: {e}")
                if fallback_video:
                    print(f"[VideoInput] Using fallback video: {fallback_video}")
                    self.file_path = fallback_video
                else:
                    raise e
        else:
            self.file_path = source

        self.cap = cv2.VideoCapture(self.file_path)

    def download_video(self, url):
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': os.path.join(self.temp_folder, '%(title)s.%(ext)s')
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info_dict)

        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            raise ValueError("Downloaded file is empty")

        print(f"[VideoInput] Downloaded video to {filename}")
        return filename

    def get_frame(self):
        if not self.cap.isOpened():
            return None

        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def release(self):
        if self.cap:
            self.cap.release()
