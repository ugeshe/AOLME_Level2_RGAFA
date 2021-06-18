#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 14:00:01 2021

@author: sherry
"""
import pygame
import random

pygame.init()

window_size = 500
window = pygame.display.set_mode((window_size, window_size))
window.fill([238, 164, 127])



image = pygame.image.load('robot.png')
image_width  = image.get_rect().size[0]
image_height = image.get_rect().size[1]
scale        = 0.6
sprite1_ori       = pygame.transform.scale(image, (int(image_width*scale), int(image_height*scale)))
sprite1 = pygame.sprite.Sprite()
sprite1.image = sprite1_ori  
sprite1.rect = pygame.Rect(*window.get_rect().center, 0, 0).inflate(sprite1_ori.get_rect().size[0],
                                                                    sprite1_ori.get_rect().size[1])
w, h = sprite1_ori.get_rect().size[0], sprite1_ori.get_rect().size[1]
sprite1.rect.center = (random.randint(w+1,window_size-w+1),
                       random.randint(h+1,window_size-h+1))



# Green rectangle
sprite2_size1 = 75
sprite2_size2 = 75
sprite2 = pygame.sprite.Sprite()
sprite2.image = pygame.Surface((sprite2_size1, sprite2_size2))
sprite2.image.fill(((0, 83, 156)))
sprite2.rect = pygame.Rect(*window.get_rect().center, 0, 0).inflate(sprite2_size1, sprite2_size2)
sprite2.rect.center = (50, 250)




all_group = pygame.sprite.Group([sprite2, sprite1])
test_group = pygame.sprite.Group([sprite2])

x_change = random.randint(1,9)
y_change = random.randint(1,9)


old_x, old_y = sprite1.rect.center
sprite1.rect.center = (old_x+x_change, old_y+x_change)
new_x, new_y = sprite1.rect.center



##


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    
    new_x, new_y = sprite1.rect.center
    
    collide = pygame.sprite.spritecollide(sprite1, test_group, False)  
    window.fill([238, 164, 127])
    all_group.draw(window)
  

    if new_x>old_x: 
        if new_x >= (window_size-w/2):
            old_x = new_x
            x=sprite1.rect.center[0]
            sprite1.rect.center = (x-x_change, new_y)
            #new_x = sprite1.rect.center[0]
        else:
            if bool(collide)==True:
                for s in collide:
                    pygame.draw.rect(window, (0, 255, 255), s.rect)
                    old_x = new_x
                    x=sprite1.rect.center[0]
                    sprite1.rect.center = (x-x_change, new_y)
                    #new_x = sprite1.rect.center[0]
                #new_x = sprite1.rect.center[0] 
            else:
                old_x = new_x
                x=sprite1.rect.center[0]
                sprite1.rect.center = (x+x_change, new_y)
                #new_x = sprite1.rect.center[0]
    else:
        if new_x <= w/2:
            old_x = new_x
            x=sprite1.rect.center[0]
            sprite1.rect.center = (x+x_change, new_y)
            #new_x = sprite1.rect.center[0]
        else:
            if bool(collide)==True:
                for s in collide:
                    pygame.draw.rect(window, (0, 255, 255), s.rect)
                    old_x = new_x
                    x=sprite1.rect.center[0]
                    sprite1.rect.center = (x+x_change, new_y)
                    #new_x = sprite1.rect.center[0]
                #new_x = sprite1.rect.center[0] 
            else:
                old_x = new_x
                old_x = new_x
                x=sprite1.rect.center[0]
                sprite1.rect.center = (x-x_change, new_y)
    
    new_x = sprite1.rect.center[0]
    
    #print('2', old_x, new_x)
    if new_y>old_y:
       
        if new_y >= (window_size-h/2):
            old_y = new_y
            y=sprite1.rect.center[1]
            sprite1.rect.center = (new_x, y-y_change)
            #new_y= sprite1.rect.center[1]
        else:
            if bool(collide)==True:
                for s in collide:
                    pygame.draw.rect(window, (0, 255, 255), s.rect)
                    old_y = new_y
                    y=sprite1.rect.center[1]
                    sprite1.rect.center = (new_x, y-y_change)
                #new_y= sprite1.rect.center[1]
            else:
                old_y = new_y
                y=sprite1.rect.center[1]
                sprite1.rect.center = (new_x, y+y_change)
                #new_y = sprite1.rect.center[1]
    else:
        
        if new_y <= h/2:
            old_y = new_y
            y=sprite1.rect.center[1]
            sprite1.rect.center = (new_x, y+y_change)
            #new_y= sprite1.rect.center[1]
        else:
            if bool(collide)==True:
                for s in collide:
                    pygame.draw.rect(window, (0, 255, 255), s.rect)
                    old_y = new_y
                    y=sprite1.rect.center[1]
                    sprite1.rect.center = (new_x, y+y_change)
                #new_y= sprite1.rect.center[1]
            else:
                old_y = new_y
                y=sprite1.rect.center[1]
                sprite1.rect.center = (new_x, y-y_change)
    
    new_y= sprite1.rect.center[1]
    
    pygame.display.flip()
    
    pygame.time.Clock().tick(80)
    
pygame.quit()
exit()













