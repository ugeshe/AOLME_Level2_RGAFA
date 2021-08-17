
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

my_video = aolme2.vid('Clock tutorial',500,700)
my_video.set_back('back1',bac)
my_video.init_video('back1', 0, 0)

my_video.set_sprite('B1',my_sprite)


######## start for loop ########
my_video.place_sprite('B1',100,250)

my_video.set_new_frame('back1',0,0)
my_video.move_sprite('B1',350,0,Trace=True)

my_video.set_new_frame('back1',0,0)
my_video.move_sprite('B1',40,40,Trace=True)

my_video.set_new_frame('back1',0,0)
my_video.move_sprite('B1',-90,30,Trace=True)

my_video.set_new_frame('back1',0,0)
my_video.move_sprite('B1',-100,-100,Trace=True)

my_video.draw_path('B1')
