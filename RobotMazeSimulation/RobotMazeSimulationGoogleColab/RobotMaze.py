#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 18:08:04 2021

@author: sherry
"""

from RobotMazeSetting3 import RobotMazeSetting

if __name__ == '__main__':
    """ Type activities for robot movemxents:
        Move forward:  gopi.fw(second)
        Move backward: gopi.bw(second)
        Move left:     gopi.lt(second)
        Move right:    gopi.rt(second)
    """
    frame_list = []


    robot_speed =  3
    gopi        =  RobotMazeSetting(robot_speed, frame_list)
    collision   =  False
    final       =  False
    
    while(final==False):
        if collision == False:
            collision, final, time = gopi.fw(10)
        else:
            collision, final = gopi.bw(4)
            collision, final = gopi.ltd(50)

        if time == False:
          break
       
            
    #gopi.run_game()

    all_frame = gopi.frame_list
    print(len(all_frame))
    fps = 25
    play_video = AOLME.vid_show(all_frame, fps)  

HTML(play_video.to_html5_video())


