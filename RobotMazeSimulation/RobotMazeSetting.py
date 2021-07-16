#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 18:25:50 2021

@author: sherry
"""
import pygame
import math

class RobotMazeSetting:
    def __init__(self, robot_speed, frame_list):
        pygame.init()
        self.speed = robot_speed
        self.bg_color   = [238, 164, 127]
        self.maze_color = [0, 83, 156]
        self.exit_color = [255, 83, 56]

        self.window_size = 500
        self.window = pygame.display.set_mode((self.window_size+300, self.window_size))
        self.window.fill(self.bg_color)
        
        # Robot
        self.image = pygame.image.load('robot.png')
        self.image_width  = self.image.get_rect().size[0]
        self.image_height = self.image.get_rect().size[1]
        self.scale        = 0.6
        self.sprite_ori  = pygame.transform.scale(self.image, (32, 32))
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = self.sprite_ori  
        self.sprite.rect = pygame.Rect(*self.window.get_rect().center, 0, 0).inflate(self.sprite_ori.get_rect().size[0],
                                                                                     self.sprite_ori.get_rect().size[1])
        self.sprite_image_copy = self.sprite_ori  
        
        
        self.sprite.rect.center = (55,480)
        self.r = int(math.sqrt(self.sprite_ori.get_rect().size[0]**2+self.sprite_ori.get_rect().size[1]**2))
        #print(self.sprite_ori.get_rect().size[0], self.sprite_ori.get_rect().size[1])
        
        self.all_list, self.maze_list, self.exit_sprite = self.gen_maze()
        self.all_group = pygame.sprite.Group(self.all_list)
        self.maze_group = pygame.sprite.Group(self.maze_list)
        self.final_group = pygame.sprite.Group([self.exit_sprite])
        self.run = True
        self.angle = 0
        self.collision = False
        self.final=False
        self.total_time = 0  
        self.frame_list = frame_list

        
    def gen_maze(self):
        sprite2 = self.gen_maze_block(30, 500, self.maze_color, 15, 250)
        sprite3 = self.gen_maze_block(30, 500, self.maze_color, 485, 250)
        sprite4 = self.gen_maze_block(400, 30, self.maze_color, 220, 15)
        sprite5 = self.gen_maze_block(400, 30, self.maze_color, 280, 485)
        sprite6 = self.gen_maze_block(30, 100, self.maze_color, 400, 250)
        sprite7 = self.gen_maze_block(150, 50, self.maze_color, 250, 150)
        sprite8 = self.gen_maze_block(50, 50,  self.maze_color, 55, 320)
        sprite9 = self.gen_maze_block(50, 30,  self.exit_color, 445, 15)
        all_list  = [self.sprite, sprite2, sprite3, sprite4, sprite5, sprite6, sprite7, sprite8, sprite9]
        maze_list = [sprite2, sprite3, sprite4, sprite5, sprite6, sprite7, sprite8]
        return all_list, maze_list, sprite9
        
        
    def gen_maze_block(self, w, h, color, x, y):
        sprite = pygame.sprite.Sprite()
        sprite.image = pygame.Surface((w, h))
        sprite.image.fill(color)
        sprite.rect = pygame.Rect(*self.window.get_rect().center, 0, 0).inflate(w, h)
        sprite.rect.center = (x, y)
        return sprite

    
            
    def check_collison(self):
        self.window.fill(self.bg_color)
        self.all_group.draw(self.window)
        
        
        if self.total_time > 10:
            #pygame.display.flip()
            myFont = pygame.font.SysFont("arial", 25)
            time_label_new   = myFont.render("Time is over!!! ", 1, (214, 49, 104))
            self.window.blit(time_label_new, (520, 200))
           
            view = pygame.surfarray.array3d(self.window)
            view = view.transpose([1, 0, 2])
            (self.frame_list).append(view)
            
            pygame.quit()
        else:
            
            myFont = pygame.font.SysFont("arial", 18)
            time_label   = myFont.render("Running time(s): ", 1, (0, 83, 156))
            time_display    = myFont.render(str(self.total_time), 1, (0, 83, 156))
        
        
            self.window.blit(time_label, (520, 200))
            self.window.blit(time_display, (700, 200))
            
            view = pygame.surfarray.array3d(self.window)
            view = view.transpose([1, 0, 2])
            (self.frame_list).append(view)
            
            
        collide = pygame.sprite.spritecollide(self.sprite, self.maze_group, False)
        final = pygame.sprite.spritecollide(self.sprite, self.final_group, False)
        if bool(final) == True:
            print('Robot is free!!!')
            self.final = True
            self.run = False
            return 
        
        if bool(collide)==True:
            self.collision = True
            print('Cannot move')
            self.run = False
            
            return 
        else:
            self.collision = False
            self.run = True
        
            pygame.display.flip()
            pygame.time.Clock().tick(40)

        return 
        

    
    
    
    def fw(self, sec):
        print('Move forward {}s'.format(sec))
        
        for i in range(0, sec+1):
            self.total_time = self.total_time + 1     
    
            old_x, old_y = self.sprite.rect.center
            if (self.angle>=0 and self.angle<=90):
                self.sprite.rect.center = (round(old_x - math.sin(self.angle/180*math.pi)*self.speed),
                                           round(old_y - math.cos(self.angle/180*math.pi)*self.speed))
            elif (self.angle>90 and self.angle<=180):
                self.sprite.rect.center = (round(old_x - math.sin((180-self.angle)/180*math.pi)*self.speed),
                                           round(old_y + math.cos((180-self.angle)/180*math.pi)*self.speed))
            elif (self.angle>180 and self.angle<=270):
                self.sprite.rect.center = (round(old_x + math.sin((self.angle-180)/180*math.pi)*self.speed),
                                           round(old_y + math.cos((self.angle-180)/180*math.pi)*self.speed))
            else:
                self.sprite.rect.center = (round(old_x + math.sin((360-self.angle)/180*math.pi)*self.speed),
                                           round(old_y - math.cos((360-self.angle)/180*math.pi)*self.speed))
        
            self.check_collison()
            if self.run == False:
                print("Cannot move forward")
                self.run_game()
                break
     
        return self.collision, self.final
    
    
    def bw(self, sec):
        print('Move backward {}s'.format(sec))
        
        for i in range(0, sec+1):
            self.total_time = self.total_time + 1     

            old_x, old_y = self.sprite.rect.center
            if (self.angle>=0 and self.angle<=90):
                self.sprite.rect.center = (round(old_x + math.sin(self.angle/180*math.pi)*self.speed),
                                           round(old_y + math.cos(self.angle/180*math.pi)*self.speed))
            elif (self.angle>90 and self.angle<=180):
                    self.sprite.rect.center = (round(old_x + math.sin((180-self.angle)/180*math.pi)*self.speed),
                                           round(old_y - math.cos((180-self.angle)/180*math.pi)*self.speed))
            elif (self.angle>180 and self.angle<=270):
                self.sprite.rect.center = (round(old_x - math.sin((self.angle-180)/180*math.pi)*self.speed),
                                           round(old_y - math.cos((self.angle-180)/180*math.pi)*self.speed))
            else:
                self.sprite.rect.center = (round(old_x - math.sin((360-self.angle)/180*math.pi)*self.speed),
                                           round(old_y + math.cos((360-self.angle)/180*math.pi)*self.speed))
        
            self.check_collison()
            if self.run == False:
                print("Cannot move backward")
                self.run_game()
                break
       
        return self.collision, self.final
    
    def rt(self, sec):
        print('Move right {}s'.format(sec))
        
        for i in range(0, sec+1):
            self.total_time = self.total_time + 1     

            old_x, old_y = self.sprite.rect.center
            if (self.angle>=0 and self.angle<=90):
                self.sprite.rect.center = (round(old_x + math.cos(self.angle/180*math.pi)*self.speed),
                                           round(old_y - math.sin(self.angle/180*math.pi)*self.speed))
            elif (self.angle>90 and self.angle<=180):
                self.sprite.rect.center = (round(old_x - math.cos((180-self.angle)/180*math.pi)*self.speed),
                                           round(old_y - math.sin((180-self.angle)/180*math.pi)*self.speed))
            elif (self.angle>180 and self.angle<=270):
                self.sprite.rect.center = (round(old_x - math.cos((self.angle-180)/180*math.pi)*self.speed),
                                           round(old_y + math.sin((self.angle-180)/180*math.pi)*self.speed))
            else:
                self.sprite.rect.center = (round(old_x + math.cos((360-self.angle)/180*math.pi)*self.speed),
                                           round(old_y + math.sin((360-self.angle)/180*math.pi)*self.speed))
        
            self.check_collison()
            if self.run == False:
                print("Cannot move right")
                self.run_game()
                break
        
        return self.collision, self.final
    
    
    def lt(self, sec):
        print('Move left {}s'.format(sec))
        
        for i in range(0, sec+1):
            self.total_time = self.total_time + 1     

            old_x, old_y = self.sprite.rect.center
            if (self.angle>=0 and self.angle<=90):
                self.sprite.rect.center = (round(old_x - math.cos(self.angle/180*math.pi)*self.speed),
                                           round(old_y + math.sin(self.angle/180*math.pi)*self.speed))
            elif (self.angle>90 and self.angle<=180):
                self.sprite.rect.center = (round(old_x + math.cos((180-self.angle)/180*math.pi)*self.speed),
                                           round(old_y + math.sin((180-self.angle)/180*math.pi)*self.speed))
            elif (self.angle>180 and self.angle<=270):
                self.sprite.rect.center = (round(old_x + math.cos((self.angle-180)/180*math.pi)*self.speed),
                                           round(old_y - math.sin((self.angle-180)/180*math.pi)*self.speed))
            else:
                self.sprite.rect.center = (round(old_x - math.cos((360-self.angle)/180*math.pi)*self.speed),
                                           round(old_y - math.sin((360-self.angle)/180*math.pi)*self.speed))
        
            self.check_collison()
            if self.run == False:
                print("Cannot move left")
                self.run_game()
                break
        
        
        return self.collision, self.final
    
    
    
    
    
    def ltd(self, angle):
        print('Turn left {} degrees'.format(angle))
        #print(self.sprite.image.get_rect().size[0], self.sprite.image.get_rect().size[1])

        """rotate an image while keeping its center"""
              
        self.angle = (self.angle + angle) % 360
        #print(self.angle)
        #self.sprite.image = pygame.transform.rotate(self.sprite.image, angle)
        self.sprite.image = pygame.transform.rotate(self.sprite_image_copy, self.angle)
        self.sprite.rect = self.sprite.image.get_rect(center=self.sprite.rect.center)
        self.check_collison()
        if self.run == False:
            print("Cannot turn left")
            self.run_game()
     
       
                
        return self.collision, self.final
    
    
    def rtd(self, angle):
        print('Turn right {} degrees'.format(angle))
        print('self.angle = ', self.angle)
        #print(self.sprite.image.get_rect().size[0], self.sprite.image.get_rect().size[1])

        """rotate an image while keeping its center"""
        #self.sprite.image = self.sprite_image_copy
        self.angle = (self.angle - angle) % 360
        #print(self.angle)
        #self.sprite.image = pygame.transform.rotate(self.sprite.image, self.angle)
        
        self.sprite.image = pygame.transform.rotate(self.sprite_image_copy, self.angle)
        
        self.sprite.rect = self.sprite.image.get_rect(center=self.sprite.rect.center)
        self.check_collison()
        if self.run == False:
            print("Cannot turn right")
            self.run_game()
            
      
                                                                   
        return self.collision, self.final 
    
    
    
    
    def run_game(self):
    
        self.window.fill(self.bg_color)
        self.all_group.draw(self.window)
        
        
        if self.run==True:
            #self.window.blit(time_label, (560, 200))
            pygame.display.flip()
            pygame.quit()
    
    
    
    
    
    