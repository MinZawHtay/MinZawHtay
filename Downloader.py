import pytube
from tqdm import tqdm
import time
import os
import re
link = input('Enter Video Link : ')
video = pytube.YouTube(link)
title = video.title
new = title.replace('|' or '#',' ')
save_path = "E:\\New folder\\mp4"
msi="E:\\New folder\\mp3"

def highest(stream):
    print(video.title)
    print('Please wait for few moment....')
    stream = video.streams.get_highest_resolution()
    for x in tqdm(range(100),
            ascii=False,
            desc="Loading"):
            time.sleep(0.001)
    print('Downloading....')
    stream.download(filename= new+'.mp4',output_path=save_path)
    for i in tqdm(range(100),
            ascii=False,desc='Downloading',
            unit='MB'):
            time.sleep(1)
    print('Done')

def lowest(lows):
        print(video.title)
        print('Please wait for few moment....')
        lows= video.streams.get_lowest_resolution()
        for x in tqdm(range(100),
            ascii=False,
            desc="Loading"):
            time.sleep(0.001)
        print('Downloading....')
        lows.download(filename= new+'.mp4',output_path=save_path)
        for i in tqdm(range(100),
            ascii=False,desc='Downloading',
            unit='MB'):
            time.sleep(1)
        print('Done')

def Music(mp3):
        print(video.title)
        print('Please wait for few moment....')
        mp3=video.streams.filter(only_audio=True).first()
        for x in tqdm(range(100),
            ascii=False,
            desc="Loading"):
            time.sleep(0.001)
        print('Downloading....')
        mp3.download(filename= new+'.mp3',output_path=msi)
        for i in tqdm(range(100),
            ascii=False,desc='Downloading',
            unit='MB'):
            time.sleep(1)
        print('Done')
while True:
    print('Video Quality')
    print('1.Highest Quality.')
    print('2.lowest Quality.')
    print('3.Music.')
    print('4.Exit.')
    
    chioce= int(input('Enter The Video Quality : '))
    if chioce == 1:
        highest(link)
        
    elif chioce == 2:
        lowest(link)

    elif chioce ==3:
        Music(link)
        
    elif chioce ==4:
        quit()
    else:
        print('Invalid Selection. Please Try Again !')