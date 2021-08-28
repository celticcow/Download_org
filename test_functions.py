#!/usr/bin/python3

import os
import magic
from os.path import expanduser

#sudo apt-get install python3-magic

def main():
    directory_to_check = "/home/gdunlap/Downloads"
    files = os.listdir(directory_to_check)

    print(directory_to_check)
    print(expanduser("~") + "/Downloads")

    for f in files:
        print(f)
        my_file = directory_to_check + "/" + f
        info = magic.from_file(my_file)
        #info = magic.from_file(f)
        if "image" in info:
            print("IMAGE FOUND")
        
        print(info)
        print("---------------------------")

if __name__ == "__main__":
    main()