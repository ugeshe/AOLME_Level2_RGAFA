# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:59:38 2020

@author: wshi
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

    detect_color = (255, 0, 0)
    gopi = RobotSimulation(detect_color)
    dis_robot_color=gopi._update_screen()
    print('dis_robot_color = ', dis_robot_color)
    gopi.fw(20)
    gopi.lt(5)
# =============================================================================
#     gopi.ltd(150)
#     gopi.lt(5)
#     gopi.bw(2)
#     gopi.rt(3)
#     gopi.ltd(45)
# =============================================================================
    
    gopi.run_game()

    
