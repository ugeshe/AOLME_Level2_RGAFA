# -*- coding: utf-8 -*-
"""
Created on Thu May 24 06:09:00 2018

@author: luis
"""

from AOLME import *

import numpy as np
import cv2
from aolme2 import *



####################### FROM LEVEL 1 #########################

total_columns = 20
total_rows = 20

frame_3 = [["FF"]*total_columns for row in range(total_rows)]

#frame 3
#background
im_fill(frame_3,[0,14],[0,19],"42cef4") #skyblue
im_fill(frame_3,[15,19],[0,19],"2d1515") #land
im_fill(frame_3,[2,4],[13,17],"fffb19") # sun yellow
im_fill(frame_3,[1,5],[14,16],"fffb19") # sun yellow


im_fill(frame_3,[2,2],[4,6],"931616")
im_fill(frame_3,[3,4],[5,5],"931616")
im_fill(frame_3,[1,1],[4,6],"931616")
frame_3[1][5] = "42cef4"

im_fill(frame_3,[1,4],[8,10],"15568e")
im_fill(frame_3,[2,4],[9,9],"15568e")
frame_3[2][9] = "42cef4"
frame_3[4][9] = "42cef4"

im_fill(frame_3,[1,2],[12,14],"3a2782")
im_fill(frame_3,[2,4],[13,13],"3a2782")
frame_3[1][13] = "42cef4"

#head
im_fill(frame_3,[6,8],[7,11],"f62217")

#left arm
im_fill(frame_3,[7,9],[6,6],"f62217")
im_fill(frame_3,[9,9],[6,8],"f62217")


#right arm
im_fill(frame_3,[7,9],[12,12],"f62217")
im_fill(frame_3,[9,9],[9,12],"f62217")


#legs
im_fill(frame_3,[10,15],[8,9],"f62217")

################################################################

#>>>>>>>>>>>>>> frame_3 is of type list, not an array

####################### FROM LEVEL 2 #########################


##################### 1. Import Background
# import background image 
bac=cv2.imread("backgroundMario.jpg")

num_rows=bac.shape[0]  # Clean 
num_cols=700

# Create new video 
myvideo = vid('First video',num_rows,num_cols)

# Add background to the video
myvideo.set_back('back1', bac)

back2=np.zeros((1000,1000,3), dtype=np.uint8)
back2[:,:,0] = 255
myvideo.set_back('back2', back2)
myvideo.show_back('back2')

# Init video at (0,100) point of the bacground
myvideo.init_video('back2',0,100)


##################### 3. Set sprite using Generate_sprite.py 

# Set test sprite with Name B1 (Bowser1)
myvideo.set_sprite('B1')


##################### 4. Design Frames for B1

# Scale and Flip Vertically
scaleB1=1.0
myvideo.scale_sprite('B1',350,450,scaleB1)

for i in range (0,3):  
    myvideo.set_new_frame('back1',0,100)    
    scaleB1=scaleB1+0.8
    myvideo.flip_vertically('B1')
    myvideo.scale_sprite('B1',350,450,scaleB1)

# Rotate and Flip Horizontally
iangle=0
icols=300
irows=300

for i in range (0,10):
    myvideo.set_new_frame('back1',0,100)
    myvideo.flip_horizontally('B1')
    myvideo.rotate_sprite('B1',irows,icols,iangle)
    iangle = iangle + 40


##################### 4. Play Video and Show Sprites

# Show Sprites

myvideo.show_back('back1')
myvideo.show_sprite('B1')


# Show last frame
myvideo.show_last_frame()

# Print in console the number of frames
print("Num of frames = {}".format(myvideo.get_num_of_frames()))

# Set to True to Debug frame by frame
""" Commented line 'cv2.destroyAllWindows()' to not close the 
    previous '.get_background' & 'get_sprite' cv2.imshow figures """
myvideo.play_video(1) 

    
# Save video with name 'test1', if not specified default name is 'output'
myvideo.save_video(25,'test1')

