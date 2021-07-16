# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 17:40:28 2017

@author: Wenjing Shi
"""

import cv2
import AOLME
import pickle

# Saving
#data = [1,2,3,4]


# Loading




back_img = cv2.imread('./images/Background.jpg')
obj_img = cv2.imread('./images/gopigo.jpg')

back_img = cv2.resize(back_img, (int(back_img.shape[1]/3), int(back_img.shape[0]/3)))
obj_img = cv2.resize(obj_img, (int(obj_img.shape[1]/6), int(obj_img.shape[0]/6)))


print('Size of background = ', back_img.shape)
print('Size of object = ', obj_img.shape)


obj_roi = AOLME.ROI(obj_img)
print (obj_roi.shape)
print (obj_roi)
pickle.dump(obj_roi, open("mask_1.pkl","wb"), protocol = 2)
mask1 = pickle.load(open("mask_1.pkl","rb"))
print (mask1.shape)
print (mask1)



