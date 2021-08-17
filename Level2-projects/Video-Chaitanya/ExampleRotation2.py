# -*- coding: utf-8 -*-
"""
Created on Wed May 30 12:42:17 2018

@author: luis
"""

import aolme2 
import cv2

# read using cv2
ExampleImage=cv2.imread('resultRotation2.png')

# Show using aolme2 command
aolme2.plot_img(ExampleImage,"Example result")


my_sprite = aolme2.spr()
my_sprite.set_sprite("clock")

bac=cv2.imread("wall.jpg")

my_video = aolme2.vid('Rotation Example 1',400,1000)
my_video.set_back('wall',bac)
my_video.init_video('wall', 0, 0)
my_video.set_sprite('clock',my_sprite)




angles=[30,-30,60]

my_video.rotate_sprite('clock',200,200,angles[0])

    
my_video.show_last_frame()
    
    

