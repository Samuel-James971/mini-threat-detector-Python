import os, time, threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import hashlib
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

WATCH_DIR = os.getenv("WATCH_DIR", "watched")
ALERTS_PATH = "data/alerts.jsonl"

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def log_alert(alert_type, file_path, old_hash=None, new_hash=None):
    Path("data").mkdir(exist_ok=True)
    with open(ALERTS_PATH, "a") as f:
        f.write(str({
            "type": alert_type,
            "path": file_path,
            "old_hash": old_hash,
            "new_hash": new_hash,
            "time": int(time.time())
        }) + "\n")
    print(f"[ALERT] {alert_type}: {file_path}")

baseline = {}

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory: return
        h = sha256_file(event.src_path)
        baseline[event.src_path] = h
        log_alert("file_created", event.src_path)

    def on_deleted(self, event):
        if event.is_directory: return
        old_hash = baseline.pop(event.src_path, None)
        log_alert("file_deleted", event.src_path, old_hash)

    def on_modified(self, event):
        if event.is_directory: return
        old_hash = baseline.get(event.src_path)
        new_hash = sha256_file(event.src_path)
        baseline[event.src_path] = new_hash
        if old_hash != new_hash:
            log_alert("file_modified", event.src_path, old_hash, new_hash)

def start(stop_event):
    Path(WATCH_DIR).mkdir(exist_ok=True)
    for f in Path(WATCH_DIR).glob("**/*"):
        if f.is_file():
            baseline[str(f)] = sha256_file(f)
    observer = Observer()
    observer.schedule(Handler(), WATCH_DIR, recursive=True)
    observer.start()
    try:
        while not stop_event.is_set():
            time.sleep(0.5)
    finally:
        observer.stop()
        observer.join()
