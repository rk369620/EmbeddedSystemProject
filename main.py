import time
from threading import Thread
import sys
import os

from src.video_input.video_input import VideoInput
from src.detection.vehicle_accident_detector import VehicleAccidentDetector
from src.logging_module.logger import EventLogger
from src.communication.communicator import Communicator
from src.ui.interface import MonitorUI

if len(sys.argv) > 1:
    VIDEO_SOURCE = sys.argv[1]
else:
    VIDEO_SOURCE = 'test_videos/sample.mp4'

LOG_FILE = 'events.json'
RPI_IP = '192.168.1.100:5000'  # Replace with  Pi IP
DETECTION_THRESHOLD = 25
MIN_CONSECUTIVE_FRAMES = 3
COOLDOWN_SECONDS = 5
FALLBACK_VIDEO = 'test_videos/sample.mp4'

video_input = VideoInput(VIDEO_SOURCE, fallback_video=FALLBACK_VIDEO)
detector = VehicleAccidentDetector(
    threshold=DETECTION_THRESHOLD,
    min_consecutive_frames=MIN_CONSECUTIVE_FRAMES,
    cooldown_seconds=COOLDOWN_SECONDS
)
logger = EventLogger(LOG_FILE)
communicator = Communicator(RPI_IP)
ui = MonitorUI(communicator=communicator)


def detection_loop():
    while True:
        frame = video_input.get_frame()
        if frame is None:
            print("[Main] End of video or cannot read frame")
            break

        detected, metadata = detector.detect(frame)

        if detected:
            logger.log("Vehicle Accident", metadata)

            communicator.send_alert("activate")

            ui.update_status("Vehicle Accident Detected!", alert=True)
        else:

            ui.update_status("System Idle", alert=False)

        # Small delay to reduce CPU usage
        time.sleep(0.1)

detection_thread = Thread(target=detection_loop, daemon=True)
detection_thread.start()

ui.run()

video_input.release()
