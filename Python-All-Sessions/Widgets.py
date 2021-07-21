#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 16:32:13 2021

@author: sherry
"""
from ipywidgets import interactive
import ipywidgets as widgets
import cv2
import matplotlib.pyplot as plt

class Widgets():
    def __init__(self, img):
        self.img = img
        (self.row, self.column, self.channel) = (self.img).shape
        
    def DisplayData(self, Row, Column, Red, Green, Blue):
        fig = plt.figure(figsize=(10, 10))
        
        plt.subplot(2,2,1)
        plt.xticks([]),plt.yticks([]) # Turn off the x and y coordinates
        plt.imshow(cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB))
        plt.title('Color Wheel Image')
        
        pixel = self.img[Row:Row+1, Column:Column+1]
        (b, g, r) = self.img[Row, Column]
        img_copy = self.img.copy()
        img_copy[max(0, Row-5):min(self.row-1, Row+5), max(0, Column-1):min(self.column-1, Column+1)] = (3, 186, 252)
        img_copy[max(0, Row-1):min(self.row-1, Row+1), max(0, Column-5):min(self.column-1, Column+5)] = (3, 186, 252)
        
        plt.subplot(2,2,2)
        plt.xticks([]),plt.yticks([]) # Turn off the x and y coordinates
        plt.imshow(cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB))
        plt.title('The seleted pixel is marked')
        
        
        # Replace the color for the selected pixel
        img_new = (self.img).copy() 
        pixel_new = img_new[Row:Row+1, Column:Column+1]
        img_new[Row, Column] = (Blue, Green, Red)
        
        plt.subplot(2,2,3)
        plt.xticks([]),plt.yticks([]) # Turn off the x and y coordinates
        plt.imshow(cv2.cvtColor(pixel_new, cv2.COLOR_BGR2RGB))
        plt.title('The new color')
        
        plt.subplot(2,2,4)
        plt.xticks([]),plt.yticks([]) # Turn off the x and y coordinates
        plt.imshow(cv2.cvtColor(img_new, cv2.COLOR_BGR2RGB))
        plt.title('New Color Wheel Image')
        
        print('\n')
        print("Pixel at ({}, {}) - Red: {}, Green: {}, Blue: {}".format(Row, Column, r,g,b))
        print("Hex = ", "#%02x%02x%02x" % (r, g, b))
        print('\n')
        print("Updating pixel at ({}, {}) - Red: {}, Green: {}, Blue: {}".format(Row, Column, Red, Green, Blue))
        print("Hex = ", "#%02x%02x%02x" % (Red, Green, Blue))