# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 11:01:17 2018

@author: Aolme7
"""

# AOLME2 classes and functions that we will be demonstrating:
from aolme2 import vid, spr, load_img, plot_img, clean, TSP, img_fill

# Use reset in IPython to clean up the variables.
# Clean() closes all of the Windows.
clean()

# Constructor for video class
videoName = "AVENGERS INFINITY BIG MAC"
num_of_rows = 500
num_of_cols = 900
my_video = vid(videoName, num_of_rows, num_of_cols)

##############################################################

# Add a FIRST BACKGROUND 
worldmap = load_img("worldmap.jpg") # Background image file
my_video.set_back('back1',worldmap )       # Save it in the video
my_video.show_back('back1')                 # Show it


 
##############################################################

# Add a FIRST SPRITE
my_1st_sprite = spr()          # Construct a sprite
my_1st_sprite.set_sprite("Big mac") # Load it from the file B1.pickle
my_1st_sprite.show("Big mac")       # Show it

#add second sprite
my_2nd_sprite = spr()          # Construct a sprite
my_2nd_sprite.set_sprite("Thanos") # Load it from the file B1.pickle
my_2nd_sprite.show("Thanos.")       # Show it

#

##############################################################

# Make the FIRST sprite available to your video:
my_sprite_name_1 = "Big mac"
my_video.set_sprite(my_sprite_name_1, my_1st_sprite)
# Make the SECOND sprite available to your video:
my_sprite_name_2 = "Thanos"
my_video.set_sprite(my_sprite_name_2, my_2nd_sprite)
# Make the SECOND sprite available to your video:
#my_sprite_name_2 = "SuperMario"
#my_video.set_sprite(my_sprite_name_2, my_2nd_sprite)


###############################################################

# Take a look at what your video knows
print(" ")
print("Video Object Information:")
print(my_video)


##############################################################

 #Create the first video frame with FIRST BACKGROUND
left_offset = 120
top_offset  = 50
my_video.init_video('back1', top_offset, left_offset)  # First video frame
#

#
# Place the big mac at russia
row_center    = 240
column_center = 800
sc = 0.5

    
my_video.scale_sprite("Big mac", row_center, column_center, sc)
    
#my_video.place_sprite(my_sprite_name_1, row_center, column_center)

# Place the big mac at USA
row_center    = 300
column_center = 100
sc = 0.5
my_video.scale_sprite("Big mac", row_center, column_center, sc)
#Place the big mac at Greenland
row_center    = 100
column_center = 250 
 #my_video.place_sprite(my_sprite_name_1, row_center, # columncenter)
my_video.scale_sprite("Big mac", row_center, column_center, sc)
my_video.show_last_frame()             # You can see the Add a second SPRITE

#
#Create New frame

my_video.set_new_frame('back1', top_offset, left_offset) 

# Place the big mac at russia
row_center    = 240
column_center = 800
sc = 0.5

    
my_video.scale_sprite("Big mac", row_center, column_center, sc)
    
#my_video.place_sprite(my_sprite_name_1, row_center, column_center)

# Place the big mac at USA
row_center    = 300
column_center = 100
sc = 0.5
my_video.scale_sprite("Big mac", row_center, column_center, sc)
#Place the big mac at Greenland
row_center    = 100
column_center = 250 
 #my_video.place_sprite(my_sprite_name_1, row_center, # columncenter)
my_video.scale_sprite("Big mac", row_center, column_center, sc)

# Place the Thanos at africa
row_center    = 400
column_center = 500
sc = 0.3

    
my_video.scale_sprite("Thanos", row_center, column_center, sc)


#MOve Thanos to Russia
#my_video.set_new_frame('back1', top_offset, left_offset) 
#sc = 0.5
my_video.show_last_frame()

#Third frame

my_video.set_new_frame('back1', top_offset, left_offset) 


#my_video.place_sprite(my_sprite_name_1, row_center, column_center)

# Place the big mac at USA
row_center    = 300
column_center = 100
sc = 0.5
my_video.scale_sprite("Big mac", row_center, column_center, sc)
#Place the big mac at Greenland
row_center    = 100
column_center = 250 
 #my_video.place_sprite(my_sprite_name_1, row_center, # columncenter)
my_video.scale_sprite("Big mac", row_center, column_center, sc)

# Place the Thanos at africa
row_center    = 240
column_center = 800
sc = 0.3

    
my_video.scale_sprite("Thanos", row_center, column_center, sc)


#MOve Thanos to Russia
#my_video.set_new_frame('back1', top_offset, left_offset) 
##sc = 0.5
#my_video.show_last_frame()    
##my_video.scale_sprite("Thanos", row_center, column_center, sc)
#
## Place the big mac at USA
#row_center    = 300
#column_center = 100
#sc = 0.5
#my_video.scale_sprite("Big mac", row_center, column_center, sc)
##Place the big mac at Greenland
#row_center    = 100
#column_center = 250 
# #my_video.place_sprite(my_sprite_name_1, row_center, # columncenter)
#my_video.scale_sprite("Big mac", row_center, column_center, sc)

my_video.show_last_frame()

#Fourth Frame 
my_video.set_new_frame('back1', top_offset, left_offset) 

# Place the big mac at russia
#row_center    = 240
#column_center = 800
#sc = 0.5

    
#
#my_video.scale_sprite("Big mac", row_center, column_center, sc)
    
#my_video.place_sprite(my_sprite_name_1, row_center, column_center)

# Place the big mac at USA
row_center    = 300
column_center = 100
sc = 0.5
my_video.scale_sprite("Big mac", row_center, column_center, sc)
#Place the big mac at Greenland
row_center    = 100
column_center = 250 
 #my_video.place_sprite(my_sprite_name_1, row_center, # columncenter)
my_video.scale_sprite("Big mac", row_center, column_center, sc)

# Place the Thanos at greenland

row_center    = 100
column_center = 250
sc = 0.3

    
my_video.scale_sprite("Thanos", row_center, column_center, sc)


#MOve Thanos to Russia
#my_video.set_new_frame('back1', top_offset, left_offset) 
#sc = 0.5
my_video.show_last_frame()
#Five Frame 
my_video.set_new_frame('back1', top_offset, left_offset) 

# Place the big mac at russia
#row_center    = 240
#column_center = 800
#sc = 0.5

    
#my_video.scale_sprite("Big mac", row_center, column_center, sc)
    
#my_video.place_sprite(my_sprite_name_1, row_center, column_center)

# Place the big mac at USA
row_center    = 300
column_center = 100
sc = 0.5
my_video.scale_sprite("Big mac", row_center, column_center, sc)
#Place the big mac at Greenland
#row_center    = 100
#column_center = 250 
# #my_video.place_sprite(my_sprite_name_1, row_center, # columncenter)
#my_video.scale_sprite("    Big mac", row_center, column_center, sc)

# Place the Thanos at usa

row_center    = 300
column_center = 100
sc = 0.3

    
my_video.scale_sprite("Thanos", row_center, column_center, sc)

#SIXTH Frame 
my_video.set_new_frame('back1', top_offset, left_offset) 

# Place the big mac at russia
#row_center    = 240
#column_center = 800
#sc = 0.5

    
#my_video.scale_sprite("Big mac", row_center, column_center, sc)
    
#my_video.place_sprite(my_sprite_name_1, row_center, column_center)

# Place the big mac at USA
#row_center    = 300
#column_center = 100
#sc = 0.5
#my_video.scale_sprite("Big mac", row_center, column_center, sc)
#Place the big mac at Greenland
#row_center    = 100
#column_center = 250 
# #my_video.place_sprite(my_sprite_name_1, row_center, # columncenter)
#my_video.scale_sprite("    Big mac", row_center, column_center, sc)

# Place the Thanos at africa

row_center    = 400
column_center = 500
sc = 0.3

    
my_video.scale_sprite("Thanos", row_center, column_center, sc)




my_video.draw_path("Thanos")





################################################
# TSP material
the_path = my_video.get_path("Thanos")
my_TSP = TSP(the_path)
my_TSP.best_tour()
my_video.play_video(1)
