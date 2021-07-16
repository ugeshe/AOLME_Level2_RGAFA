#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 14:35:45 2021

@author: sherry
"""

from robotSimulation import RobotSimulation

      
if __name__ == '__main__':
    # Make a game instance, and run the game.
       
    """ Type activities for robot movemxents:
        Move forward:  gopi.fw(second)
        Move backward: gopi.bw(second)
        Move left:     gopi.lt(second)
        Move right:    gopi.rt(second)
        Turn left:     gopi.ltd(degree)
        Turn right:    gopi.rtd(degree)
    """
    red_range   = [50, 255]
    green_range = [0, 90]
    blue_range  = [0, 60]

    detect_color    = (red_range, green_range, blue_range)
    gopi            = RobotSimulation(detect_color)
    dis_robot_color = gopi._update_screen()
    collision       = False
    
    while(dis_robot_color>10):
        
        if collision == False:
            collision = gopi.fw(1)
            
        else:
            gopi.lt(1)
            gopi.bw(1)
            gopi.rtd(90)
            gopi.fw(3)
            gopi.ltd(90)
            
            collision = False
        dis_robot_color=gopi._update_screen()
        
    gopi.run_game()
    



