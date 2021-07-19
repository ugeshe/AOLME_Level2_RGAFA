# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 16:06:04 2020

@author: wshi
"""

import sys
from sys import exit
import pygame
from settings import Settings
from robot import Robot
from maze import Maze
# =============================================================================
# from mario import Mario
# from snoopy import Snoopy
# from panda import Panda
# from lobo import Lobo
# =============================================================================
import matplotlib.pyplot as plt
import math

class RobotSimulation:
    """ Overall class to manage game assets and behavior. """
    
    def __init__(self, detect_color, frame_list):
        """ Initialize the game and create game resources. """
        pygame.init()
        self.settings = Settings()
        self.screen   = pygame.display.set_mode((self.settings.screen_width, 
                                               self.settings.screen_height))
        pygame.display.set_caption("Robot Simulation")
        self.screen.fill(self.settings.bg_color)
        
        self.red_rect_position = (300,250,50,50)
        self.yellow_rect_position = (200,450,50,50)
        self.detect_color = detect_color
        
        
# =============================================================================
#         self.mario    = Mario(self)
#         self.snoopy   = Snoopy(self)
#         self.panda    = Panda(self)
#         self.lobo     = Lobo(self)
# =============================================================================
        
        pygame.draw.rect(self.screen, (255, 83, 56), self.red_rect_position)
        pygame.draw.rect(self.screen, (255, 255, 0), self.yellow_rect_position)
        self.view_ori = pygame.surfarray.array3d(self.screen)
        #  convert from (width, height, channel) to (height, width, channel)
        self.view = self.view_ori.transpose([1, 0, 2])
        
        #plt.imshow(self.view)
        #plt.show()
        self.robot    = Robot(self)
        self.maze     = Maze(self)
        
        self.movement = False
        self.total_time = 0      
        self.frame_list = frame_list
        self.time = True
        
    def fw(self, sec):
        for i in range(1, sec+1):
            self.total_time = self.total_time + 1
            self.robot.movement = True
            collision = self.robot.fw()
            self.robot.update()
            self.maze.draw_maze()
            self._update_screen()
        return collision, self.time
            
            
            
    def bw(self, sec):
        for i in range(1, sec+1):
            self.total_time = self.total_time + 1
            self.robot.movement = True  
            collision = self.robot.bw()
            self.robot.update()
            self.maze.draw_maze()
            self._update_screen()
        return collision, self.time
        #return dis_robot_color
            
    def rt(self, sec):
        for i in range(1, sec+1):
            self.total_time = self.total_time + 1
            self.robot.movement = True
            collision = self.robot.rt()
            self.robot.update()
            self.maze.draw_maze()
            self._update_screen()
        return collision, self.time
        #return dis_robot_color
            
    def lt(self, sec):
        for i in range(1, sec+1):
            self.total_time = self.total_time + 1
            self.robot.movement = True  
            collision = self.robot.lt()
            self.robot.update()
            self.maze.draw_maze()
            self._update_screen()
        return collision, self.time
        #return dis_robot_color
            
    def rtd(self, angle):
        self.robot.movement = True
        self.robot.rtd(angle)
        self.robot.update()
        self.maze.draw_maze()
        self._update_screen()
        #return dis_robot_color
        
    def ltd(self, angle):
        self.robot.movement = True
        self.robot.ltd(angle)
        self.robot.update()
        self.maze.draw_maze()
        self._update_screen()
        #return dis_robot_color
        
    def run_game(self):
        """ Start the main loop for the game. """
        
        while True:
            
           
            if self.movement:
                #print(self.movement)
                self.maze.draw_maze()
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
        
        x, y = self.robot.rect.x, self.robot.rect.y
        color_x, color_y = (self.red_rect_position[0]+int(self.red_rect_position[2]/2),
                            self.red_rect_position[1]+int(self.red_rect_position[3]/2))
        print(color_x, color_y)
        (r,g,b) = self.view[y][x]
        print('Robot position = ({}, {})    Color(r, g, b) = ({}, {}, {})'. 
              format(x, y, r, g, b))
        
        
        
        dis_robot_color = math.sqrt((x-color_x)**2 + (y-color_y)**2)
       
        myFont = pygame.font.SysFont("arial", 18)
        myFont2 = pygame.font.SysFont("arial", 26)
        
        distance_label =  myFont.render("Distance:", 3, (0, 83, 156))
        robot_color_label  = myFont.render("Robot--Color: ", 1, (0, 83, 156))
        color_label     = myFont.render("Color(r, g, b): ", 1, (0, 83, 156))
        time_label   = myFont.render("Running time(s): ", 1, (0, 83, 156))
        
        ### pass a string to myFont.render
        dis_display   = myFont.render(str(int(dis_robot_color)), 1, (0, 83, 156))
        color_r_display = myFont.render(str(r), 1, (0, 83, 156))
        color_g_display = myFont.render(str(g), 1, (0, 83, 156))
        color_b_display = myFont.render(str(b), 1, (0, 83, 156))
        time_display    = myFont.render(str(self.total_time), 1, (0, 83, 156))
        message_1 =myFont2.render("YOU FIND THE COLOR!!!", 5, (30, 130, 53))
        message_2 =myFont2.render("DETECTING......",5, (214, 49, 104))
        
        red_min   = self.detect_color[0][0]       
        red_max   = self.detect_color[0][1]
        green_min = self.detect_color[1][0]       
        green_max = self.detect_color[1][1]
        blue_min  = self.detect_color[2][0]       
        blue_max  = self.detect_color[2][1]
        
# =============================================================================
#         print('set color for detection:')
#         print(red_min, red_max)
#         print(green_min, green_max)
#         print(blue_min, blue_max)
#  
#         print('detected color:', r, g, b)
# =============================================================================
        

        if (r<=red_max and r>=red_min) and (g<=green_max and g>=green_min) and (b<=blue_max and b>=blue_min):
        
        #    (r, g, b) == self.detect_color:
            print('Detect color')
            self._check_events()
            self.screen.fill(self.settings.bg_color)
            pygame.draw.rect(self.screen, (255, 83, 56), self.red_rect_position)
            pygame.draw.rect(self.screen, (255, 255, 0), self.yellow_rect_position)
            
            self.screen.blit(distance_label, (560, 50))
            self.screen.blit(robot_color_label, (560, 100))
            self.screen.blit(dis_display, (700, 100))
            
            self.screen.blit(color_label, (560, 150))
            self.screen.blit(color_r_display, (700, 150))
            self.screen.blit(color_g_display, (750, 150))
            self.screen.blit(color_b_display, (800, 150))
            
            if self.total_time > 100:
                myFont = pygame.font.SysFont("arial", 25)
                time_label_new   = myFont.render("Time is over!!! ", 1, (214, 49, 104))
                self.screen.blit(time_label_new, (560, 200))
                
                view = pygame.surfarray.array3d(self.screen)
                view = view.transpose([1, 0, 2])
                (self.frame_list).append(view)
                
                self.time = False
            
            else:
                self.screen.blit(time_label, (560, 200))
                self.screen.blit(time_display, (700, 200))
                view = pygame.surfarray.array3d(self.screen)
                view = view.transpose([1, 0, 2])
                (self.frame_list).append(view)
            
            self.screen.blit(message_1, (600, 300))
            
            self.robot.blitme()
            self.maze.draw_maze()
            
            pygame.display.flip()
            #pygame.display.quit()
            
            #exit()
        
        else:
            self._check_events()
            self.screen.fill(self.settings.bg_color)
            pygame.draw.rect(self.screen, (255, 83, 56), self.red_rect_position)
            pygame.draw.rect(self.screen, (255, 255, 0), self.yellow_rect_position)
        
        
        
#        self.screen.blit(self.settings.bg_image, (0,0))

            self.screen.blit(distance_label, (560, 50))
            self.screen.blit(robot_color_label, (560, 100))
            self.screen.blit(dis_display, (700, 100))
            
            self.screen.blit(color_label, (560, 150))
            self.screen.blit(color_r_display, (700, 150))
            self.screen.blit(color_g_display, (750, 150))
            self.screen.blit(color_b_display, (800, 150))
            
            if self.total_time > 100:
                myFont = pygame.font.SysFont("arial", 25)
                time_label_new   = myFont.render("Time is over!!! ", 1, (214, 49, 104))
                self.screen.blit(time_label_new, (560, 200))
                
                view = pygame.surfarray.array3d(self.screen)
                view = view.transpose([1, 0, 2])
                (self.frame_list).append(view)
                
            else:
                self.screen.blit(time_label, (560, 200))
                self.screen.blit(time_display, (700, 200))
                
                view = pygame.surfarray.array3d(self.screen)
                view = view.transpose([1, 0, 2])
                (self.frame_list).append(view)
                
                
            self.screen.blit(message_2, (600, 300))
        
            self.robot.blitme()
            self.maze.draw_maze()
# =============================================================================
#         self.mario.blitme()
#         self.snoopy.blitme()
#         self.panda.blitme()
#         self.lobo.blitme()
# =============================================================================
        # Make the most recently drawn screen visible.q
            pygame.display.flip()
            
        
        return dis_robot_color
        
                        


    def rot_center(self, angle):

        center = self.robot.image.get_rect().center
        rotated_image = pygame.transform.rotate(self.robot.image, angle)
        new_rect = rotated_image.get_rect(center = center)
        self.robot.image = rotated_image
        
        return rotated_image, new_rect   


