
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:06:09 2017

@author: Wenjing Shi
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
aolme = AOLME.Robot('GopigoChallenge.avi', back_rows, back_cols, speed)

aolme.add_back('Backgound', back_img)
aolme.add_obj('Robot', obj_img, obj_roi) 
aolme.add_obj_rot('Robot', 'r', 0)


""" Create the first frame"""
aolme.init_video('Backgound', 0, 0)

""" Ready to start """
for i in range (1, 35):
    aolme.new_frame(0, 0)
    aolme.place_obj('Robot', 557, 182)  # (577,182)
    


""" Robot's movement """

aolme.fw(2)      # Moves forward for 2 seconds
aolme.rt(90)     # Turns right by 90 degrees
aolme.fw(1.6)    # Moves forward for 1.6 seconds
aolme.lt(135)    # Turns left by 135 degrees
aolme.fw(2.2)    # Moves forward for 2.2 seconds
aolme.bw(2.2)    # Moves backward for 2.2 seconds
aolme.rt(45)     # Turns right by 45 degrees
aolme.fw(2)      # Moves forward for 2 seconds
aolme.rt(90)     # Turns right by 90 degrees
aolme.fw(2)      # Moves forward for 2 seconds
aolme.rt(90)     # Turns right by 90 degrees
aolme.fw(3.5)    # Moves forward for 3.5 seconds
aolme.rt(90)     # Turns right by 90 degrees
aolme.fw(4)      # Moves forward for 4 seconds
aolme.rt(155)    # Turns right by 155 degrees
aolme.fw(3)      # Moves forward for 3 seconds

""" Beep """
#aolme.beep1()    # Play a single notes
#aolme.beep2()    # Play two different notes
#aolme.beep3()    # Play four different notes
#aolme.beepLong() # Play short melody

""" Destroy all windows """
aolme.save_video()
aolme.play_video()


aolme.out.release()
cv2.destroyAllWindows()

