# -*- coding: utf-8 -*-
from moviepy.editor import VideoFileClip,concatenate_videoclips
a=[[10,20],
   [15,25],
   [20,30],
   [40,50]]
createVar=locals()
con=[]
for i in range(len(a)):
    video=VideoFileClip("test.mp4").subclip(a[i][0],a[i][1])
   
    createVar['clip'+str(i)]=video
    con.append(locals()['clip'+str(i)])
final_clip=concatenate_videoclips(con)
final_clip.write_videofile("final.mp4",fps=25)
