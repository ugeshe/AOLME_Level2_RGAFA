#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 18:16:35 2020

@author: sherry
"""
import pygame
import numpy as np
#import matplotlib.pyplot as plt

class Maze():
    """ A class to manage the maze """
    def __init__(self, rs_game):
        """ Initialize the maze's settings """
        self.screen        = rs_game.screen
        self.settings      = rs_game.settings
        self.maze_width    = 17
        self.maze_height   = 19
        self.square_width  = 32
        self.square_height = 32
        self.maze_color    = (0, 83, 156)
        #self.maze_mask     = np.zeros((self.settings.screen_width, self.settings.screen_height))
# =============================================================================
#         self.maze          = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                               0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,
#                               0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0,
#                               0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
#                               0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0,
#                               0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0,
#                               0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
#                               0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0,
#                               0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0,
#                               0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0,
#                               0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0,
#                               0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,
#                               0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0,
#                               0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0,
#                               0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0,
#                               0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0,
#                               0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0,
#                               0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
#                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# =============================================================================
        self.maze          = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
                              0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0,
                              0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
                              0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0,
                              0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0,
                              0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0,
                              0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
                              0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
                              0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
                              0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0,
                              0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,
                              0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,
                              0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
                              0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0,
                              0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0,
                              0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
                              0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    

# =============================================================================
#         self.maze_width  = self.settings.screen_width - 2*self.settings.robot_margin
#         self.maze_height = self.settings.screen_height - 2*self.settings.robot_margin
#     
# =============================================================================
    def draw_square(self, squ_x, squ_y):
        
        pygame.draw.rect(self.screen, 
                         self.maze_color, 
                         [squ_x, squ_y, self.square_width, self.square_height], 
                         0)
        
# =============================================================================
#          pygame.draw.rect(self.screen, 
#                          self.maze_color, 
#                          [0, 50 , self.square_width, self.square_height], 
#                          0)
# =============================================================================
    
    def draw_maze(self):
        """ Draw the maze """
        bx = 0
        by = 0
        squ_x = 0
        squ_y = 0
        
        for i in range(0,self.maze_width * self.maze_height):
            
            if self.maze[i] == 0:
                self.draw_square(squ_x, squ_y)
            
            squ_x = squ_x + self.square_width
            bx = bx + 1
            
            if bx > self.maze_width-1:
                bx = 0 
                by = by + 1
                squ_x = 0
                squ_y = squ_y + self.square_height
                
    def gen_maze_mask(self):
        mx = 0
        my = 0
        mask_x = 0
        mask_y = 0
        maze_mask = np.zeros((self.settings.screen_height, self.settings.screen_width))
        for i in range(0,self.maze_width * self.maze_height):
            if self.maze[i] == 1:
                maze_mask[mask_y:mask_y+self.square_height, mask_x:mask_x+self.square_width]=1
                
            
            mask_x = mask_x + self.square_width
            mx = mx + 1
            
            if mx > self.maze_width-1:
                mx = 0 
                my = my + 1
                mask_x = 0
                mask_y = mask_y + self.square_height
       
        return maze_mask
        
        
            
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        