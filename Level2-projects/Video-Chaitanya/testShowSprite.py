
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 12:42:17 2018

@author: luis
"""

import aolme2 
import cv2

my_sprite = aolme2.spr()
my_sprite.set_sprite("clock")

my_sprite.show('Clock sprite')


bac=cv2.imread("wall.JPG")

my_video = aolme2.vid('Clock tutorial',2000,2000)
my_video.set_back('back1',bac)
my_video.init_video('back1', 50, 50)

#my_video.show_back('back1')

my_video.set_sprite('clock',my_sprite)

my_video.rotate_sprite('clock',1000,1000,0)

my_video.show_last_frame()