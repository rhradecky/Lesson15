import threading
import time

def background_task():
    while True:
        print("Daemo thread is running")
        time.sleep(2)

daemon_thread = threading.Thread(target=background_task, args=(),daemon=True)
daemon_thread.start()

print("zacni program")
time.sleep(11)
print("ukonci program")
