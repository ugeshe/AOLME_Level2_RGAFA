# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 22:03:51 2020

@author: wshi
"""

import sys
import pygame

class Settings:
    """ A class to store all settings for Robot Simulation """
    
    def __init__(self):
        """ Initialize the game's settings """
        # Screen settings
        self.screen_width  = 544 + 400
        self.screen_height = 608
        
        self.bg_color      = (238, 164, 127)
        
# =============================================================================
#         self.image = pygame.image.load("./images/bg.png")
#         self.image_width  = self.image.get_rect().size[0]
#         self.image_height = self.image.get_rect().size[1]
#         self.scale        = 0.7
#         self.bg_image     = pygame.transform.scale(self.image, (int(self.image_width*self.scale), int(self.image_height*self.scale)))
#         #
#         self.screen_width  = self.bg_image.get_rect().size[0]
#         self.screen_height = self.bg_image.get_rect().size[1]
# =============================================================================
        # Robot settings
        self.robot_speed   = 10
        self.robot_margin  = 10