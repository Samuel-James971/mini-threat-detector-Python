import threading, signal, time
from src import file_monitor, network_monitor

stop_event = threading.Event()

def handle_sig(sig, frame):
    print("Shutting down...")
    stop_event.set()

signal.signal(signal.SIGINT, handle_sig)
signal.signal(signal.SIGTERM, handle_sig)

t1 = threading.Thread(target=file_monitor.start, args=(stop_event,))
t2 = threading.Thread(target=network_monitor.start, args=(stop_event,))
t1.start()
t2.start()

print("Monitoring started. Press Ctrl+C to stop.")
try:
    while not stop_event.is_set():
        time.sleep(1)
except KeyboardInterrupt:
    stop_event.set()

t1.join()
t2.join()
print("Monitoring stopped.")
