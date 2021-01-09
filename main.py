from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_listen):
            src = folder_listen + "/" + filename
            new_file = new_folder + "/" + filename
            print(f"Copy {src} to {new_file}")
            os.rename(src, new_file)

folder_listen = '' # Ej. '/home/user/folder_org'
new_folder = '' # Ej. '/home/user/folder_dest'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_listen, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
