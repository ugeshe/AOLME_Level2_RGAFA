# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 11:02:20 2018

@author: Aolme10
"""

# AOLME2 classes and functions that we will be demonstrating:
from aolme2 import vid, spr, load_img, plot_img, clean, TSP, img_fill

# Use reset in IPython to clean up the variables.
# Clean() closes all of the Windows.
clean()
def backcopy():
    # Create the first video frame with FIRST BACKGROUND
    left_offset = 0
    top_offset  = 100
    my_video.init_video('back1', top_offset, left_offset)  # First video frame
    
    # Place the third SPRITE
    #h1
    row_center    = 400
    col_center = 200
    scaleFactor = .10
    my_video.scale_sprite("pilebricks", row_center, col_center, scaleFactor)
    #h2
    row_center    = 320
    col_center = 100
    scaleFactor = .10
    my_video.scale_sprite("pilebricks", row_center, col_center, scaleFactor)
    #h3
    row_center    = 350
    col_center = 370
    scaleFactor = .10
    my_video.scale_sprite("pilebricks", row_center, col_center, scaleFactor)
    #h4
    row_center    = 330
    col_center = 450
    scaleFactor = .09
    my_video.scale_sprite("pilebricks", row_center, col_center, scaleFactor)
    #h5
    row_center    = 340
    col_center = 725
    scaleFactor = .10
    my_video.scale_sprite("pilebricks", row_center, col_center, scaleFactor)

# Constructor for video class
videoName = "Video1"
num_of_rows = 500
num_of_cols = 800
my_video = vid(videoName, num_of_rows, num_of_cols)

##############################################################

# Add a FIRST BACKGROUND 
backhood = load_img("neighborhood.png") # Background image file
my_video.set_back('back1', backhood)       # Save it in the video
my_video.show_back('back1')                 # Show it


# Add a first SPRITE
my_1st_sprite = spr()             # Construct a sprite
my_1st_sprite.set_sprite("fix it felix") # Load it from the file B1.pickle
my_1st_sprite.show("fix it felix")       # Show it


# Add a SECOND SPRITE
my_2nd_sprite = spr()             # Construct a sprite
my_2nd_sprite.set_sprite("sbcar") # Load it from the file B1.pickle
my_2nd_sprite.show("sbcar")       # Show it


# Add a third SPRITE
my_3rd_sprite = spr()             # Construct a sprite
my_3rd_sprite.set_sprite("pilebricks") # Load it from the file B1.pickle
my_3rd_sprite.show("pilebricks")      # Show it


# Make the FIRST sprite available to your video:
my_sprite_name_1 = "fix it felix"
my_video.set_sprite(my_sprite_name_1, my_1st_sprite)

# Make the SECOND sprite available to your video:
my_sprite_name_2 = "sbcar"
my_video.set_sprite(my_sprite_name_2, my_2nd_sprite)


# Make the THIRD sprite available to your video:
my_sprite_name_3 = "pilebricks"
my_video.set_sprite(my_sprite_name_3, my_3rd_sprite)

# Take a look at what your video knows
print("sbcar")
print("Video Object Information:")
print(my_video)

# Create the first video frame with FIRST BACKGROUND
backcopy()
# Place the SECOND SPRITE
row_center    = 400
col_center = 100
scaleFactor = 0.12
#my_video.flip_hor("sbcar", row_center, col_center)
my_video.scale_sprite("sbcar", row_center, col_center, scaleFactor)

backcopy()

row_center    = 320
col_center = 100
scaleFactor = 0.12
#my_video.flip_hor("sbcar", row_center, col_center)
my_video.scale_sprite("sbcar", row_center, col_center, scaleFactor)

backcopy()

row_center    = 350
col_center = 370
scaleFactor = 0.12
#my_video.flip_hor("sbcar", row_center, col_center)
my_video.scale_sprite("sbcar", row_center, col_center, scaleFactor)

backcopy()

row_center    = 330
col_center = 450
scaleFactor = 0.12
#my_video.flip_hor("sbcar", row_center, col_center)
my_video.scale_sprite("sbcar", row_center, col_center, scaleFactor)

backcopy()

row_center    = 340
col_center = 725
scaleFactor = 0.12
#my_video.flip_hor("sbcar", row_center, col_center)
my_video.scale_sprite("sbcar", row_center, col_center, scaleFactor)


my_video.show_last_frame()  # You can see the frame

# Draw the video path:
my_video.draw_path("sbcar")

################################################
# TSP material
the_path = my_video.get_path("sbcar")
my_TSP = TSP(the_path)
my_TSP.best_tour()

my_video.play_video(0.5)





