#!/usr/bin/python
import random
import os
import subprocess


def absoluteFilePaths(directory):
    return_list = []
    
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            if f.endswith((".mp3")):
                FullFileName=os.path.abspath(os.path.join(dirpath, f))
                print FullFileName
                return_list.append(FullFileName)
    
    return return_list



folder_location = '/home/pi/music'
file_list = absoluteFilePaths(folder_location)
wordlen=len(file_list)
os.system('modprobe snd_bcm2835')
os.system('amixer cset numid=3 1')
while True:
     print "--------------------------------"
     i=random.randint(0, wordlen)
     subprocess.call('mpg321 '+file_list[i], shell=True)
