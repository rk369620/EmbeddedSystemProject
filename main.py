import time
from threading import Thread
import sys
import os
import cv2

from src.video_input.video_input import VideoInput
from src.detection.vehicle_accident_detector import VehicleAccidentDetector
from src.logging_module.logger import EventLogger
from src.communication.communicator import Communicator
from src.ui.interface import MonitorUI

VIDEO_PATH = None
USE_WEBCAM = False

if len(sys.argv) > 1:
    arg = sys.argv[1].lower()
    if arg == "--webcam":
        USE_WEBCAM = True

    elif arg == "--video" and len(sys.argv) > 2:
        VIDEO_PATH = sys.argv[2]
    else:
        print("Invalid argument. Usage: --video <path> OR --webcam")
        sys.exit(1)
else:

    VIDEO_PATH = 'test_videos/accident.mp4'


LOG_FILE = "events.json"
RPI_IP = "192.168.0.105:5000"

THRESHOLD = 2
MIN_FRAMES = 3
COOLDOWN = 5
ALERT_HOLD_SECONDS = 8

video_input = VideoInput(source=VIDEO_PATH, use_webcam=USE_WEBCAM)

detector = VehicleAccidentDetector(
    threshold=THRESHOLD,
    min_consecutive_frames=MIN_FRAMES,
    cooldown_seconds=COOLDOWN
)

logger = EventLogger(LOG_FILE)
communicator = Communicator(RPI_IP)
ui = MonitorUI(communicator)

video_finished = False
alert_active = False
last_alert_time = None


def detection_loop():
    global video_finished, alert_active, last_alert_time

    while True:
        frame = video_input.get_frame()
        if frame is None:
            print("[Main] Video finished")
            communicator.send_alert("deactivate")
            ui.update_status("Video Finished", alert=False)
            video_finished = True
            break

        # Detect accidents
        detected, meta = detector.detect(frame)

        # Display video
        cv2.imshow("Accident Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            video_finished = True
            break

        current_time = time.time()


        if detected:

            if not last_alert_time or current_time - last_alert_time > COOLDOWN:
                print("[Main] 🚨 ACCIDENT DETECTED")
                logger.log("Vehicle Accident", meta)
                communicator.send_alert("activate")
                ui.update_status("Vehicle Accident Detected!", alert=True)

                alert_active = True
                last_alert_time = current_time

        elif alert_active:
            # Keep alert active for minimum hold time
            if current_time - last_alert_time > ALERT_HOLD_SECONDS:
                print("[Main] Alert hold finished → Deactivating")
                communicator.send_alert("deactivate")
                ui.update_status("System Idle", alert=False)
                alert_active = False

        time.sleep(0.03)


    video_input.release()
    cv2.destroyAllWindows()
    print("[Main] Detection stopped")


def check_exit():
    if video_finished:
        ui.root.after(0, ui.root.destroy)
    else:
        ui.root.after(200, check_exit)


Thread(target=detection_loop, daemon=True).start()
ui.root.after(200, check_exit)
ui.run()

print("[Main] Application exited cleanly")
