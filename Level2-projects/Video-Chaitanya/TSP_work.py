# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 11:41:56 2018

@author: Aolme7
"""

from aolme2 import TSP


city_coords=[[4,0],[2,2],[5,3],[5,6],[4,9],[1,6],[9,5]]
my_TSP =TSP(city_coords)
tour1 =[1,2,3,4,6,5,7,1]
tour1_len=my_TSP.tour_length(tour1)
print("tour=",tour1,"has length",tour1_len)
my_TSP.plot_tour(tour1,100,100)


city_coords=[[4,0],[2,2],[1,6],[4,9],[9,5],[5,6],[5,3]]
my_TSP =TSP(city_coords)
tour1 =[1,2,5,6,7,4,3,1]
tour1_len=my_TSP.tour_length(tour1)
print("tour=",tour1,"has length",tour1_len)
my_TSP.plot_tour(tour1,100,100)