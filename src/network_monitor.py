import time, os
from dotenv import load_dotenv

load_dotenv()
DETECTION_TEST_MODE = int(os.getenv("DETECTION_TEST_MODE", "1"))

def start(stop_event):
    print("Network monitor running in safe test mode.")
    while not stop_event.is_set():
        time.sleep(2)
        if DETECTION_TEST_MODE:
            print("[TEST MODE] Detected test IP 192.0.2.1")
