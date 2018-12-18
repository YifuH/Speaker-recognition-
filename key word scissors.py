# -*- coding: utf-8 -*-
import re
from collections import Counter
from moviepy.editor import VideoFileClip, concatenate

def assemble_cuts(cuts, outputfile):
    final = concatenate([video.subclip(start, end)
                         for (start,end) in cuts])
    final.to_videofile(outputfile)

def convert_time(timestring):
    nums = list(map(float, re.findall(r'\d+', timestring)))
    return 3600*nums[0] + 60*nums[1] + nums[2] + nums[3]/1000

with open("TBBT_S12E09.srt") as f:
    lines = f.readlines()

times_texts = []
current_times , current_text = None, ""

for line in lines:
    times = re.findall("[0-9]*:[0-9]*:[0-9]*,[0-9]*", line)
    if times != []:
        current_times = list(map(convert_time, times))
    elif line == '\n':
        times_texts.append((current_times, current_text))
        current_times, current_text = None, ""
    elif current_times is not None:
        current_text = current_text + line.replace("\n"," ")

whole_text = " ".join([text for (time, text) in times_texts])
all_words = re.findall("\w+", whole_text)
counter = Counter([w.lower() for w in all_words if len(w)>5])
cuts = [times for (times,text) in times_texts
        if (re.findall("should",text) != [])]
video = VideoFileClip("TBBT_S12E09.mkv")

assemble_cuts(cuts, "111.mp4")
