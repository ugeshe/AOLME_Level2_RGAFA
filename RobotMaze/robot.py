# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 22:10:13 2020

@author: wshi
"""

import pygame
from maze import Maze
import re
import math
from mario import Mario
from snoopy import Snoopy
from panda import Panda
from lobo import Lobo
#import matplotlib.pyplot as plt
#import matplotlib

#matplotlib.use('TkAgg')
class Robot:
    """ A class to manage the robot """
    
    def __init__(self, rs_game):
        """ Initialize the robot and set its starting position """
        self.screen      = rs_game.screen
        self.settings    = rs_game.settings
        self.maze        = Maze(self)
        self.screen_rect = rs_game.screen.get_rect()
        
        # Load the robot image and get its rect.
        self.image = pygame.image.load('./images/robot.png')
        self.image_width  = self.image.get_rect().size[0]
        self.image_height = self.image.get_rect().size[1]
        self.scale        = 0.55
        self.image        = pygame.transform.scale(self.image, (int(self.image_width*self.scale), int(self.image_height*self.scale)))
        self.rect         = self.image.get_rect()
        self.mario    = Mario(self)
        self.snoopy   = Snoopy(self)
        self.panda    = Panda(self)
        self.lobo     = Lobo(self)
        self.angle    = 0
# =============================================================================
#         # Start each new robot on the screen
#         self.rect.bottom = self.screen_rect.bottom - self.settings.robot_margin
#         self.rect.right  = self.screen_rect.right/2
# =============================================================================
        # Start each new robot on the screen
        self.rect.bottom = 570
        self.rect.right  = 254
        # Store decimal values for the robot's both horizontal and vertival position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Movement flag
        self.moving_right = False
        self.moving_left  = False
        self.moving_up    = False
        self.moving_down  = False
        self.movement     = False
    
    def movefw(self):
        pygame.time.delay(100)
        if self.movement and self.rect.top > self.settings.robot_margin and self.maze.gen_maze_mask()[math.floor(self.y - self.settings.robot_speed)][math.floor(self.x+self.image.get_rect().size[0])] == 1 and self.maze.gen_maze_mask()[math.floor(self.y - self.settings.robot_speed)][math.floor(self.x)] == 1:
            self.y -= self.settings.robot_speed
         
            #print("forward", self.rect.x, self.rect.y)
                
    def movebw(self):
        pygame.time.delay(100)       
        if  self.movement and self.rect.bottom < self.screen_rect.bottom - self.settings.robot_margin and self.maze.gen_maze_mask()[math.floor(self.y + self.image.get_rect().size[1]+ self.settings.robot_speed)][math.floor(self.x+self.image.get_rect().size[0])] == 1 and self.maze.gen_maze_mask()[math.floor(self.y + self.image.get_rect().size[1]+ self.settings.robot_speed)][math.floor(self.x)] == 1:
            self.y += self.settings.robot_speed
         
            #print("back", self.rect.x, self.rect.y)
            
    def movefrt(self):
        pygame.time.delay(100)
        if self.movement and self.rect.right  < self.screen_rect.right - self.settings.robot_margin and  self.maze.gen_maze_mask()[math.floor(self.y+ self.image.get_rect().size[1])][math.floor(self.x + self.settings.robot_speed+self.image.get_rect().size[0])]==1 and self.maze.gen_maze_mask()[math.floor(self.y)][math.floor(self.x + self.settings.robot_speed+self.image.get_rect().size[0])]==1:
            self.x += self.settings.robot_speed
            
            #print("right", self.rect.x, self.rect.y)
                
    def moveflt(self):
        pygame.time.delay(100)
        if  self.movement and self.rect.left > self.settings.robot_margin and  self.maze.gen_maze_mask()[math.floor(self.y+ self.image.get_rect().size[1])][math.floor(self.x - self.settings.robot_speed)] == 1 and self.maze.gen_maze_mask()[math.floor(self.y)][math.floor(self.x - self.settings.robot_speed)] == 1:
            self.x -= self.settings.robot_speed
            
            #print("left", self.rect.x, self.rect.y)
    
        
    
    def fw(self):
        pygame.time.delay(300)     
        if self.movement:            
            if (self.angle>=0 and self.angle<=90 and 
                self.rect.top > self.settings.robot_margin
                and self.rect.left > self.settings.robot_margin):
               
                if (self.maze.gen_maze_mask()[math.floor(self.y - math.cos(self.angle/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] - math.sin(self.angle/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y - math.cos(self.angle/180*math.pi)*self.settings.robot_speed)][math.floor(self.x - math.sin(self.angle/180*math.pi)*self.settings.robot_speed)] == 1):
                    
                    self.x = self.x - math.sin(self.angle/180*math.pi)*self.settings.robot_speed
                    self.y = self.y - math.cos(self.angle/180*math.pi)*self.settings.robot_speed
                    #print("Move forward", self.rect.x, self.rect.y)
                    
            elif (self.angle>90 and self.angle<=180 and 
                  self.rect.bottom < self.screen_rect.bottom - self.settings.robot_margin
                  and self.rect.left > self.settings.robot_margin):
                
                if (self.maze.gen_maze_mask()[math.floor(self.y + math.cos((180-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] - math.sin((180-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y + math.cos((180-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x - math.sin((180-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1
                and self.maze.gen_maze_mask()[math.floor(self.y + self.image.get_rect().size[1] + math.cos((180-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] - math.sin((180-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y + self.image.get_rect().size[1] + math.cos((180-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x - math.sin((180-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1):
                    
                    self.x = self.x - math.sin((180-self.angle)/180*math.pi)*self.settings.robot_speed
                    self.y = self.y + math.cos((180-self.angle)/180*math.pi)*self.settings.robot_speed
                    #print("Move forward", self.rect.x, self.rect.y)
                    
            elif (self.angle>180 and self.angle<=270 and
                  self.rect.bottom < self.screen_rect.bottom - self.settings.robot_margin
                  and self.rect.right  < self.screen_rect.right - self.settings.robot_margin):
                
                if (self.maze.gen_maze_mask()[math.floor(self.y + math.cos((self.angle-180)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] + math.sin((self.angle-180)/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y + math.cos((self.angle-180)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + math.sin((self.angle-180)/180*math.pi)*self.settings.robot_speed)] == 1
                and self.maze.gen_maze_mask()[math.floor(self.y + self.image.get_rect().size[1] + math.cos((self.angle-180)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] + math.sin((self.angle-180)/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y + self.image.get_rect().size[1] + math.cos((self.angle-180)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + math.sin((self.angle-180)/180*math.pi)*self.settings.robot_speed)] == 1):
                    
                    self.x = self.x + math.sin((self.angle-180)/180*math.pi)*self.settings.robot_speed
                    self.y = self.y + math.cos((self.angle-180)/180*math.pi)*self.settings.robot_speed     
                    #print("Move forward", self.rect.x, self.rect.y)
            
            elif (self.angle>270 and self.angle<=360 and
                  self.rect.top > self.settings.robot_margin
                  and self.rect.right  < self.screen_rect.right - self.settings.robot_margin):
                
                if (self.maze.gen_maze_mask()[math.floor(self.y - math.cos((360-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] + math.sin((360-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y - math.cos((360-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + math.sin((360-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1):
                    
                    self.x = self.x + math.sin((360-self.angle)/180*math.pi)*self.settings.robot_speed
                    self.y = self.y - math.cos((360-self.angle)/180*math.pi)*self.settings.robot_speed
                    #print("Move forward", self.rect.x, self.rect.y)
            
            else:
                print('Cannot move forward')
        
    def bw(self):
        pygame.time.delay(300)
        if  self.movement:
            if (self.angle>=0 and self.angle<=90 and 
                self.rect.bottom < self.screen_rect.bottom - self.settings.robot_margin
                and self.rect.right  < self.screen_rect.right - self.settings.robot_margin):
                
                if(self.maze.gen_maze_mask()[math.floor(self.y + math.cos(self.angle/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] + math.sin(self.angle/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y + math.cos(self.angle/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + math.sin(self.angle/180*math.pi)*self.settings.robot_speed)] == 1
                and self.maze.gen_maze_mask()[math.floor(self.y + self.image.get_rect().size[1] + math.cos(self.angle/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] + math.sin(self.angle/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y + self.image.get_rect().size[1] + math.cos(self.angle/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + math.sin(self.angle/180*math.pi)*self.settings.robot_speed)] == 1):
                    
                    self.x = self.x + math.sin(self.angle/180*math.pi)*self.settings.robot_speed
                    self.y = self.y + math.cos(self.angle/180*math.pi)*self.settings.robot_speed
                    #print("Move backward", self.rect.x, self.rect.y)
                    
            elif (self.angle>90 and self.angle<=180 and
                  self.rect.top > self.settings.robot_margin
                  and self.rect.right  < self.screen_rect.right - self.settings.robot_margin):
                
                if(self.maze.gen_maze_mask()[math.floor(self.y - math.cos((180-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] + math.sin((180-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y - math.cos((180-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + math.sin((180-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1):
                    
                    self.x = self.x + math.sin((180-self.angle)/180*math.pi)*self.settings.robot_speed
                    self.y = self.y - math.cos((180-self.angle)/180*math.pi)*self.settings.robot_speed
                    #print("Move backward", self.rect.x, self.rect.y)
                    
            elif (self.angle>180 and self.angle<=270 and
                  self.rect.top > self.settings.robot_margin
                  and self.rect.left > self.settings.robot_margin):
                
                if(self.maze.gen_maze_mask()[math.floor(self.y - math.cos((self.angle-180)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] - math.sin((self.angle-180)/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y - math.cos((self.angle-180)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x - math.sin((self.angle-180)/180*math.pi)*self.settings.robot_speed)] == 1):
                    
                    self.x = self.x - math.sin((self.angle-180)/180*math.pi)*self.settings.robot_speed
                    self.y = self.y - math.cos((self.angle-180)/180*math.pi)*self.settings.robot_speed 
                    #print("Move backward", self.rect.x, self.rect.y)
                    
            elif (self.angle>270 and self.angle<=360 and
                  self.rect.bottom < self.screen_rect.bottom - self.settings.robot_margin
                  and self.rect.left > self.settings.robot_margin):
                
                if(self.maze.gen_maze_mask()[math.floor(self.y + math.cos((360-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0]  - math.sin((360-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y + math.cos((360-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x  - math.sin((360-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1
                and self.maze.gen_maze_mask()[math.floor(self.y + self.image.get_rect().size[1] + math.cos((360-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0]  - math.sin((360-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y + self.image.get_rect().size[1] + math.cos((360-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x  - math.sin((360-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1):
                   
                    self.x = self.x - math.sin((360-self.angle)/180*math.pi)*self.settings.robot_speed
                    self.y = self.y + math.cos((360-self.angle)/180*math.pi)*self.settings.robot_speed
                    #print("Move backward", self.rect.x, self.rect.y)
            else:
                print("Cannot move backward")
                
    def rt(self):
        pygame.time.delay(300)
        if  self.movement:
            if (self.angle>=0 and self.angle<=90 and
                self.rect.top > self.settings.robot_margin
                  and self.rect.right  < self.screen_rect.right - self.settings.robot_margin):
                
                if (self.maze.gen_maze_mask()[math.floor(self.y - math.sin(self.angle/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] + math.cos(self.angle/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y - math.sin(self.angle/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + math.cos(self.angle/180*math.pi)*self.settings.robot_speed)] == 1):
                    
                    self.x = self.x + math.cos(self.angle/180*math.pi)*self.settings.robot_speed
                    self.y = self.y - math.sin(self.angle/180*math.pi)*self.settings.robot_speed
                    #print("Move right", self.rect.x, self.rect.y)
                    
            elif (self.angle>90 and self.angle<=180 and
                  self.rect.top > self.settings.robot_margin
                and self.rect.left > self.settings.robot_margin):
               
                if (self.maze.gen_maze_mask()[math.floor(self.y - math.sin((180-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] - math.cos((180-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y - math.sin((180-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x - math.cos((180-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1):
                    
                    self.x = self.x - math.cos((180-self.angle)/180*math.pi)*self.settings.robot_speed
                    self.y = self.y - math.sin((180-self.angle)/180*math.pi)*self.settings.robot_speed
                    #print("Move right", self.rect.x, self.rect.y)
                    
            elif (self.angle>180 and self.angle<=270 and
                  self.rect.bottom < self.screen_rect.bottom - self.settings.robot_margin
                  and self.rect.left > self.settings.robot_margin):
                
                if (self.maze.gen_maze_mask()[math.floor(self.y + math.sin((self.angle-180)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] - math.cos((self.angle-180)/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y + math.sin((self.angle-180)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x - math.cos((self.angle-180)/180*math.pi)*self.settings.robot_speed)] == 1
                and self.maze.gen_maze_mask()[math.floor(self.y + self.image.get_rect().size[1] + math.sin((self.angle-180)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] - math.cos((self.angle-180)/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y + self.image.get_rect().size[1] + math.sin((self.angle-180)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x - math.cos((self.angle-180)/180*math.pi)*self.settings.robot_speed)] == 1):
                    
                    self.x = self.x - math.cos((self.angle-180)/180*math.pi)*self.settings.robot_speed
                    self.y = self.y + math.sin((self.angle-180)/180*math.pi)*self.settings.robot_speed  
                    #print("Move right", self.rect.x, self.rect.y)
                    
            elif (self.angle>270 and self.angle<=360 and
                  self.rect.bottom < self.screen_rect.bottom - self.settings.robot_margin
                  and self.rect.right  < self.screen_rect.right - self.settings.robot_margin):
                
                if (self.maze.gen_maze_mask()[math.floor(self.y + math.sin((360-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] + math.cos((360-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y + math.sin((360-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + math.cos((360-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1
                and self.maze.gen_maze_mask()[math.floor(self.y + self.image.get_rect().size[1] + math.sin((360-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] + math.cos((360-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y + self.image.get_rect().size[1] + math.sin((360-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + math.cos((360-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1):
                    
                    self.x = self.x + math.cos((360-self.angle)/180*math.pi)*self.settings.robot_speed
                    self.y = self.y + math.sin((360-self.angle)/180*math.pi)*self.settings.robot_speed
                    #print("Move right", self.rect.x, self.rect.y)
            else:
                print("Cannot move right")
    
    def lt(self):
        pygame.time.delay(300)
        if self.movement:
            if (self.angle>=0 and self.angle<=90 and
                self.rect.bottom < self.screen_rect.bottom - self.settings.robot_margin
                  and self.rect.left > self.settings.robot_margin):
                
                if (self.maze.gen_maze_mask()[math.floor(self.y + math.sin(self.angle/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] - math.cos(self.angle/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y + math.sin(self.angle/180*math.pi)*self.settings.robot_speed)][math.floor(self.x - math.cos(self.angle/180*math.pi)*self.settings.robot_speed)] == 1
                and self.maze.gen_maze_mask()[math.floor(self.y + self.image.get_rect().size[1] + math.sin(self.angle/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] - math.cos(self.angle/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y + self.image.get_rect().size[1] + math.sin(self.angle/180*math.pi)*self.settings.robot_speed)][math.floor(self.x - math.cos(self.angle/180*math.pi)*self.settings.robot_speed)] == 1):
                    
                    self.x = self.x - math.cos(self.angle/180*math.pi)*self.settings.robot_speed
                    self.y = self.y + math.sin(self.angle/180*math.pi)*self.settings.robot_speed
                    #print("Move left", self.rect.x, self.rect.y)
            
            elif (self.angle>90 and self.angle<=180 and
                  self.rect.bottom < self.screen_rect.bottom - self.settings.robot_margin
                  and self.rect.right  < self.screen_rect.right - self.settings.robot_margin):
                
                if (self.maze.gen_maze_mask()[math.floor(self.y + math.sin((180-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] + math.cos((180-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y + math.sin((180-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + math.cos((180-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1
                and self.maze.gen_maze_mask()[math.floor(self.y + self.image.get_rect().size[1] + math.sin((180-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] + math.cos((180-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y + self.image.get_rect().size[1] + math.sin((180-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + math.cos((180-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1):
                
                    self.x = self.x + math.cos((180-self.angle)/180*math.pi)*self.settings.robot_speed
                    self.y = self.y + math.sin((180-self.angle)/180*math.pi)*self.settings.robot_speed
                    #print("Move left", self.rect.x, self.rect.y)
            
            elif (self.angle>180 and self.angle<=270 and
                  self.rect.top > self.settings.robot_margin
                  and self.rect.right  < self.screen_rect.right - self.settings.robot_margin):
                
                if (self.maze.gen_maze_mask()[math.floor(self.y - math.sin((self.angle-180)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] + math.cos((self.angle-180)/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y - math.sin((self.angle-180)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + math.cos((self.angle-180)/180*math.pi)*self.settings.robot_speed)] == 1):
                  
                    self.x = self.x + math.cos((self.angle-180)/180*math.pi)*self.settings.robot_speed
                    self.y = self.y - math.sin((self.angle-180)/180*math.pi)*self.settings.robot_speed               
                    #print("Move left", self.rect.x, self.rect.y)
            
            elif (self.angle>270 and self.angle<=360 and
                  self.rect.top > self.settings.robot_margin
                and self.rect.left > self.settings.robot_margin):
               
                if (self.maze.gen_maze_mask()[math.floor(self.y - math.sin((360-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x + self.image.get_rect().size[0] - math.cos((360-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1 
                and self.maze.gen_maze_mask()[math.floor(self.y - math.sin((360-self.angle)/180*math.pi)*self.settings.robot_speed)][math.floor(self.x - math.cos((360-self.angle)/180*math.pi)*self.settings.robot_speed)] == 1):
                
                    self.x = self.x - math.cos((360-self.angle)/180*math.pi)*self.settings.robot_speed
                    self.y = self.y - math.sin((360-self.angle)/180*math.pi)*self.settings.robot_speed
                    #print("Move left", self.rect.x, self.rect.y) 
    
            else:
                print("Cannot move left")
                    
        
    
    
    def rtd(self, angle):
        """rotate an image while keeping its center"""
        
        if (self.rect.bottom < self.screen_rect.bottom - self.settings.robot_margin
            and self.rect.top > self.settings.robot_margin
            and self.rect.left > self.settings.robot_margin
            and self.rect.right  < self.screen_rect.right - self.settings.robot_margin):
            
            radius_img = math.sqrt(self.image.get_rect().size[0]**2+self.image.get_rect().size[1]**2)/2
            
            if (self.maze.gen_maze_mask()[math.floor(self.rect.center[1]-radius_img)][self.rect.center[0]]==1
                and self.maze.gen_maze_mask()[math.floor(self.rect.center[1]+radius_img)][self.rect.center[0]]==1
                and self.maze.gen_maze_mask()[math.floor(self.rect.center[1])][math.floor(self.rect.center[0]-radius_img)]==1
                and self.maze.gen_maze_mask()[math.floor(self.rect.center[1])][math.floor(self.rect.center[0]+radius_img)]==1):
                
                self.angle = (self.angle - angle) % 360
                self.image = pygame.transform.rotate(self.image, 360-angle)
                self.rect = self.image.get_rect(center=self.rect.center)
                #print("Turn right", self.rect.x, self.rect.y, self.angle)
            
            else:
                print("Error1: Cannot turn right")
                #self.bw()
        else:
            print("Error2: Cannot turn right")
        
    def ltd(self, angle):
        """rotate an image while keeping its center"""
        
       
        if(self.rect.bottom < self.screen_rect.bottom - self.settings.robot_margin
           and self.rect.top > self.settings.robot_margin
           and self.rect.left > self.settings.robot_margin
           and self.rect.right  < self.screen_rect.right - self.settings.robot_margin):
            
           radius_img = math.sqrt(self.image.get_rect().size[0]**2+self.image.get_rect().size[1]**2)/2
            
           if (self.maze.gen_maze_mask()[math.floor(self.rect.center[1]-radius_img)][self.rect.center[0]]==1
               and self.maze.gen_maze_mask()[math.floor(self.rect.center[1]+radius_img)][self.rect.center[0]]==1
               and self.maze.gen_maze_mask()[math.floor(self.rect.center[1])][math.floor(self.rect.center[0]-radius_img)]==1
               and self.maze.gen_maze_mask()[math.floor(self.rect.center[1])][math.floor(self.rect.center[0]+radius_img)]==1):
               
               self.angle = (self.angle + angle) % 360
               self.image = pygame.transform.rotate(self.image, angle)
               self.rect = self.image.get_rect(center=self.rect.center)
               #print("Turn left", self.rect.x, self.rect.y, self.angle)
               
           else:
              #self.image = pygame.transform.rotate(self.image, 360-self.angle)
              print("Error1: Cannot turn left")
              #print(self.rect.x, self.rect.y, self.angle)
              #self.bw()
        
        else:
            print("Error2: Cannot turn left")


    def distance(self):
        dis_robot_panda  = math.sqrt((self.rect.x-self.panda.rect.x)**2 + (self.rect.y-self.panda.rect.y)**2)
        dis_robot_mario  = math.sqrt((self.rect.x-self.mario.rect.x)**2 + (self.rect.y-self.mario.rect.y)**2)
        dis_robot_snoopy = math.sqrt((self.rect.x-self.snoopy.rect.x)**2 + (self.rect.y-self.snoopy.rect.y)**2)
        dis_robot_lobo   = math.sqrt((self.rect.x-self.lobo.rect.x)**2 + (self.rect.y-self.lobo.rect.y)**2)
        myFont = pygame.font.SysFont("'arial", 18)
        
        distance_label =  myFont.render("Distance:", 3, (0, 83, 156))
        panda_label  = myFont.render("Robot--Panda: ", 1, (0, 83, 156))
        mario_label  = myFont.render("Robot--Mario: ", 1, (0, 83, 156))
        snoopy_label = myFont.render("Robot--Snoopy: ", 1, (0, 83, 156))
        lobo_label   = myFont.render("Robot--Lobo: ", 1, (0, 83, 156))
        
        ### pass a string to myFont.render
        panda_display  = myFont.render(str(int(dis_robot_panda)), 1, (0, 83, 156))
        mario_display  = myFont.render(str(int(dis_robot_mario)), 1, (0, 83, 156))
        snoopy_display = myFont.render(str(int(dis_robot_snoopy)), 1, (0, 83, 156))
        lobo_display   = myFont.render(str(int(dis_robot_lobo)), 1, (0, 83, 156))
        
        self.screen.blit(distance_label, (560, 50))
        self.screen.blit(panda_label, (560, 100))
        self.screen.blit(mario_label, (560, 150))
        self.screen.blit(snoopy_label, (560, 200))
        self.screen.blit(lobo_label, (560, 250))
        
        self.screen.blit(panda_display, (700, 100))
        self.screen.blit(mario_display, (700, 150))
        self.screen.blit(snoopy_display, (700, 200))
        self.screen.blit(lobo_display, (700, 250))
        
        return dis_robot_panda, dis_robot_mario, dis_robot_snoopy, dis_robot_lobo
        #print(dis_robot_panda)
        
    def update(self):
        """ Update the robot's position based on the movement flag """  
        # Update the robot's x and y values, not the rect.
        
# =============================================================================
#         maze_mask = self.maze.gen_maze_mask()
#         #plt.figure('maze')
#         plt.imshow(maze_mask)
#         plt.show()
# =============================================================================
        self.rect.x = self.x
        self.rect.y = self.y
        
        #print(self.rect.x, self.rect.y)
            
        
    def blitme(self):
        """ Draw the robot at its current location """
        self.distance()
        self.screen.blit(self.image, self.rect)        