# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 00:41:36 2020

@author: wshi
"""

import cv2
import AOLME
import pickle

#im = cv2.imread('frame_2.png')
back_img = cv2.imread('./images/Background.jpg')
obj_img = cv2.imread('./images/gopigo.jpg')
obj_roi = pickle.load(open("mask.pkl","rb"))

back_img = cv2.resize(back_img, (int(back_img.shape[1]/3), int(back_img.shape[0]/3)))
obj_img = cv2.resize(obj_img, (int(obj_img.shape[1]/6), int(obj_img.shape[0]/6)))


print('Size of background = ', back_img.shape)
print('Size of object = ', obj_img.shape)




speed = 150 # Set the speed of movement 150px/s

(back_rows, back_cols) = back_img.shape[:2]
