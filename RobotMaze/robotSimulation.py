# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 16:06:04 2020

@author: wshi
"""
import numpy as np
import sys
import pygame
from settings import Settings
from robot import Robot
from maze import Maze
from mario import Mario
from snoopy import Snoopy
from panda import Panda
from lobo import Lobo
import cv2
from google.colab.patches import cv2_imshow
from google.colab import output
import time 


class RobotSimulation:
    """ Overall class to manage game assets and behavior. """
    
    def __init__(self, frame_list):
        """ Initialize the game and create game resources. """
        pygame.init()
        
        self.settings = Settings()
        self.screen   = pygame.display.set_mode((self.settings.screen_width, 
                                               self.settings.screen_height))
        pygame.display.set_caption("Robot Simulation")
        self.robot    = Robot(self)
        self.maze     = Maze(self)
        self.mario    = Mario(self)
        self.snoopy   = Snoopy(self)
        self.panda    = Panda(self)
        self.lobo     = Lobo(self)
        self.movement = False
        self.frame_list = frame_list
           
        
        
    def fw(self, sec):
        for i in range(1, sec+1):
            self.robot.movement = True
            self.robot.fw()
            self.robot.update()
            self.maze.draw_maze()
            self._update_screen()
            
    def bw(self, sec):
        for i in range(1, sec+1):
            self.robot.movement = True  
            self.robot.bw()
            self.robot.update()
            self.maze.draw_maze()
            self._update_screen()
            
    def rt(self, sec):
        for i in range(1, sec+1):
            self.robot.movement = True
            self.robot.rt()
            self.robot.update()
            self.maze.draw_maze()
            self._update_screen()
            
    def lt(self, sec):
        for i in range(1, sec+1):
            self.robot.movement = True  
            self.robot.lt()
            self.robot.update()
            self.maze.draw_maze()
            self._update_screen()
            
    def rtd(self, angle):
        self.robot.movement = True
        self.robot.rtd(angle)
        self.robot.update()
        self.maze.draw_maze()
        self._update_screen()
        
    def ltd(self, angle):
        self.robot.movement = True
        self.robot.ltd(angle)
        self.robot.update()
        self.maze.draw_maze()
        self._update_screen()
        
    def run_game(self):
        """ Start the main loop for the game. """
        
        while True:
            
            self._check_events()
            
            if self.movement:
                #print(self.movement)
                self.maze.draw_maze()
                
# =============================================================================
#                 print(activity)
#                 self.fw(8)
#                 self.ltd(320) 
#                 
#                 self.rt(5)
#                 #self.lt(2)
#                 #self.rt(2)
# =============================================================================

                self.movement = False
            else:
               
                self.robot.update()
                self.maze.draw_maze()
                self._update_screen()

               

            
            
            
                       
    def _check_events(self):
        """ Respond to kqeypresses and mouse events """
        #self.robot.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                 self._check_keyup_events(event)
        
            
            
    def _check_keydown_events(self,event):
        """ Respond to keypresses """ 

        if event.key ==pygame.K_q:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_x:
            self.robot.movement = True
            self.movement = self.robot.movement

        
            
            
    def _check_keyup_events(self,event):
        """ Respond to releases """ 
        if event.key == pygame.K_RIGHT:
            self.robot.moving_right = False
        if event.key == pygame.K_LEFT:
            self.robot.moving_left  = False
        if event.key == pygame.K_UP:
            self.robot.moving_up    = False
        if event.key == pygame.K_DOWN:
            self.robot.moving_down  = False       
                
    def _update_screen(self):
        """ Update images on the screen, and flip to the new screen """
        self.screen.fill(self.settings.bg_color)
#        self.screen.blit(self.settings.bg_image, (0,0))
        self.robot.blitme()
        self.maze.draw_maze()
        self.mario.blitme()
        self.snoopy.blitme()
        self.panda.blitme()
        self.lobo.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()


        view = pygame.surfarray.array3d(self.screen)
        #  convert from (width, height, channel) to (height, width, channel)
        view = view.transpose([1, 0, 2])

        #  convert from rgb to bgr
        #img_bgr = cv2.cvtColor(view, cv2.COLOR_RGB2BGR)
        #print('1 = ', len(self.frame_list))
        (self.frame_list).append(view)
        #self.frame_list=[self.frame_list, img_bgr]
        #print('2 = ', len(self.frame_list))

        
        
        #Display image, clear cell every 0.5 seconds
        #cv2_imshow(img_bgr)
        #time.sleep(1)
        #output.clear()



    def rot_center(self, angle):

        center = self.robot.image.get_rect().center
        rotated_image = pygame.transform.rotate(self.robot.image, angle)
        new_rect = rotated_image.get_rect(center = center)
        self.robot.image = rotated_image
        
        return rotated_image, new_rect   


