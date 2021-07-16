# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 03:52:48 2020

@author: wshi
"""


from robot_simulation import RobotSimulation
from robot import Robot

class Gopi:
    def __init__(self):
        self.rs = RobotSimulation()
        self.robot = Robot()
        
    def fw(self, sec):
        for i in range(1, sec+1):
            self.robot.movement = True
            self.robot.fw()
            self.robot.update()
            #self.maze.draw_maze()
            self.rs._update_screen()
            
    def bw(self, sec):
        for i in range(1, sec+1):
            self.robot.movement = True  
            self.robot.bw()
            self.robot.update()
            #self.maze.draw_maze()
            self.rs._update_screen()
            
    def rt(self, sec):
        for i in range(1, sec+1):
            self.robot.movement = True
            self.robot.rt()
            self.robot.update()
            #self.maze.draw_maze()
            self.rs._update_screen()
            
    def lt(self, sec):
        for i in range(1, sec+1):
            self.robot.movement = True  
            self.robot.lt()
            self.robot.update()
            #self.maze.draw_maze()
            self.rs._update_screen()