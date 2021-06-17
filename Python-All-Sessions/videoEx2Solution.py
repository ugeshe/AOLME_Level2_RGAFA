
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 19:43:21 2018

@author: luis
"""

import cv2
import aolme2


# Init example sprite
my_sprite = aolme2.spr()
my_sprite.set_sprite("B1")

# Init video
bac=cv2.imread("backgroundMario.JPG")

my_video = aolme2.vid('Clock tutorial',560,900)
my_video.set_back('back1',bac)
my_video.init_video('back1', 0, 100)

my_video.set_sprite('B1',my_sprite)


######## start for loop ########
scaleX=1

for i in range(3):
    scaleX = scaleX + 0.5
    my_video.scale_sprite('B1',300,100+300*i,scaleX)

# Show last frame
my_video.show_last_frame()    





