#!/usr/bin/python3

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
#pip3 install watchdog
#sudo apt-get install python3-magic

import os
import json
import time
import magic

"""
download handler that inhearttes from file system event handler
"""
class DownloadHandler(FileSystemEventHandler):
    #constructor
    #worried about the /home/<user>/Downloads
    def __init__(self, folder_to_track):
        self.folder_to_track = folder_to_track
        #self.dest_root = dest_root

    def on_modified(self, event):
        debug = 1
        for filename in os.listdir(self.folder_to_track):
            src = self.folder_to_track + "/" + filename

            try:
                file_info = magic.from_file(src)

                """
                need to make a function for sub folder /type and os.rename
                """
                if "IMAGE" in file_info.upper():
                    if(debug == 1):
                        print("found image") #debug 
                    new_destination = self.folder_to_track + "/images/" + filename
                    os.rename(src, new_destination)
                elif "PDF" in file_info.upper():
                    if(debug == 1):
                        print("found pdf") 
                    new_destination = self.folder_to_track + "/pdf/" + filename
                    os.rename(src, new_destination)
                elif "WORD" in file_info.upper():
                    if(debug == 1):
                        print("found word doc") 
                    new_destination = self.folder_to_track + "/word/" + filename
                    os.rename(src, new_destination)
            except IsADirectoryError:
                pass
            #new_destination = folder_destination + "/" + filename
            #print(filename)
            #os.rename(src, new_destination)


def main():
    folder_to_track = "/home/gdunlap/Desktop/myFolder"
    #folder_destination = "/home/gdunlap/Desktop/newfolder"

    event_handler = DownloadHandler(folder_to_track)
    observer = Observer()
    observer.schedule(event_handler, folder_to_track, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    main()
#end of download_org