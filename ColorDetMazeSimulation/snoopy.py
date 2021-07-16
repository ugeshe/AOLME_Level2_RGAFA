# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 00:19:11 2020

@author: wshi
"""

import pygame
#from maze import Maze
class Snoopy:
    """ A class to manage the robot """
    
    def __init__(self, rs_game):
        """ Initialize the robot and set its starting position """
        self.screen      = rs_game.screen      
        self.screen_rect = rs_game.screen.get_rect()
        
        # Load the robot image and get its rect.
        self.image        = pygame.image.load('./images/Snoopy.png')
        self.image_width  = self.image.get_rect().size[0]
        self.image_height = self.image.get_rect().size[1]
        self.scale        = 0.5
        self.image        = pygame.transform.scale(self.image, (int(self.image_width*self.scale), int(self.image_height*self.scale)))
        
        self.rect  = self.image.get_rect()

        # Start each new robot on the screen
        self.rect.bottom = 65
        self.rect.right  = 510 
      
          
    def blitme(self):
        """ Draw the robot at its current location """
        self.screen.blit(self.image, self.rect)      