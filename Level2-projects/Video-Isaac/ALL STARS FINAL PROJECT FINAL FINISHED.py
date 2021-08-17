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
def backcopy(i):
    # Create the first video frame with FIRST BACKGROUND
    left_offset = 0
    top_offset  = 100
    my_video.init_video('back1', top_offset, left_offset)  # First video frame
    
    # Place the third SPRITE
    #h1
    scaleFactor = 0.25
    if i < 5:
        row_center    = 400
        col_center = 200
        my_video.scale_sprite("pilebricks", row_center, col_center, scaleFactor)
    else:
        my_video.scale_sprite("finishedhouse", 400, 200, scaleFactor)
    #h2
    if i < 4:
        row_center    = 320
        col_center = 100
        my_video.scale_sprite("pilebricks", row_center, col_center, scaleFactor)
    else:
        my_video.scale_sprite("finishedhouse", 320, 100, scaleFactor)
    #h3
    if i < 3:
        row_center    = 300
        col_center = 300
        my_video.scale_sprite("pilebricks", row_center, col_center, scaleFactor)
    else:
        my_video.scale_sprite("finishedhouse", 300, 300, scaleFactor)
    #h4
    if i < 2:
        row_center    = 330
        col_center = 500
        my_video.scale_sprite("pilebricks", 330, 450, scaleFactor)

    else:
        my_video.scale_sprite("finishedhouse", 330, 500, scaleFactor)

    #h5
    if i < 1:
        row_center    = 340
        col_center = 725
        my_video.scale_sprite("pilebricks", row_center, col_center, scaleFactor)
    else:        
        my_video.scale_sprite("finishedhouse", 340, 725, scaleFactor)







# Constructor for video class
videoName = "Video1"
num_of_rows = 500
num_of_cols = 800
my_video = vid(videoName, num_of_rows, num_of_cols)

##############################################################

# Add a FIRST BACKGROUND 
backhood = load_img("neighborhood.png") # Background image file
my_video.set_back('back1', backhood)       # Save it in the video
#my_video.show_back('back1')                 # Show it

# Add a FIRST SPRITE
my_1st_sprite = spr()          # Construct a sprite
my_1st_sprite.set_sprite("fix it felix") # Load it from the file B1.pickle
#my_1st_sprite.show("fix it felix")       # Show it


# Add a SECOND SPRITE
my_2nd_sprite = spr()             # Construct a sprite
my_2nd_sprite.set_sprite("sbcar") # Load it from the file B1.pickle
#my_2nd_sprite.show("sbcar")       # Show it

# Add a third SPRITE
my_3rd_sprite = spr()             # Construct a sprite
my_3rd_sprite.set_sprite("pilebricks") # Load it from the file B1.pickle
#my_3rd_sprite.show("pilebricks")      # Show it

# Add a Fourth SPRITE
my_4rd_sprite = spr()             # Construct a sprite
my_4rd_sprite.set_sprite("finishedhouse") # Load it from the file B1.pickle
#my_4rd_sprite.show("finishedhouse")       # Show it

# Add a Fifith SPRITE
my_5nd_sprite = spr()             # Construct a sprite
my_5nd_sprite.set_sprite("sbcar") # Load it from the file B1.pickle
#my_5nd_sprite.show("sbcar")       # Show it

########################################################################
# Make the FIRST sprite available to your video:
my_sprite_name_1 = "fix it felix"
my_video.set_sprite(my_sprite_name_1, my_1st_sprite)

# Make the SECOND sprite available to your video:
my_sprite_name_2 = "sbcar"
my_video.set_sprite(my_sprite_name_2, my_2nd_sprite)


# Make the THIRD sprite available to your video:
my_sprite_name_3 = "pilebricks"
my_video.set_sprite(my_sprite_name_3, my_3rd_sprite)

# Make the foruth sprite available to your video:
my_sprite_name_4 = "finishedhouse"
my_video.set_sprite(my_sprite_name_4, my_4rd_sprite)

# Make the fifth sprite available to your video:
my_sprite_name_5 = "sbcar"
my_video.set_sprite(my_sprite_name_5, my_2nd_sprite)



# Create the first video frame with FIRST BACKGROUND
i = 0
backcopy(i)

#Place the First Sprite "FIX IT FELIX"
row_center    = 400
column_center = 700
sc=0.5
my_video.scale_sprite("fix it felix", row_center, column_center, sc)


# Create the  video frame with BACKGROUND
i +=1
backcopy(i)
#Place the First Sprite "fix it felix"
row_center    = 340
column_center = 720
sc=0.5
my_video.scale_sprite("fix it felix", row_center, column_center, sc)

i +=1
backcopy(i)
#Place the First Sprite "fix it felix"
row_center    = 330
column_center = 500
sc=0.5
my_video.scale_sprite("fix it felix", row_center, column_center, sc)

# Create the first video frame with FIRST BACKGROUND
i += 1
backcopy(i)

#Place the First Sprite "fix it felix"
row_center    = 300
column_center = 300
sc=0.5
my_video.scale_sprite("fix it felix", row_center, column_center, sc)

# Create the first video frame with FIRST BACKGROUND
i+=1
backcopy(i)
#Place the First Sprite "fix it felix"
row_center    = 320
column_center = 100
sc=0.5
my_video.scale_sprite("fix it felix", row_center, column_center, sc)

i+=1
backcopy(i)

row_center    = 400
column_center = 200
sc=0.5
my_video.scale_sprite("fix it felix", row_center, column_center, sc)

#####################################################################################

backcopy(i)

row_center = 450
col_center = 50
scaleFactor = 0.12
my_video.scale_sprite("sbcar", row_center, col_center, scaleFactor)


backcopy(i)

row_center    = 400
col_center = 200
scaleFactor = 0.12
#my_video.flip_hor("sbcar", row_center, col_center)
#my_video.move_sprite("sbcar", -50, 150)
my_video.scale_sprite("sbcar", row_center, col_center, scaleFactor)




backcopy(i)

row_center    = 320
col_center = 100
scaleFactor = 0.12
#my_video.flip_hor("sbcar", row_center, col_center)
#my_video.move_sprite("sbcar", -80, -100)
my_video.scale_sprite("sbcar", row_center, col_center, scaleFactor)


backcopy(i)

row_center    = 300
col_center = 300
scaleFactor = 0.12
#my_video.flip_hor("sbcar", row_center, col_center)
#my_video.move_sprite("sbcar", 30, 270)
my_video.scale_sprite("sbcar", row_center, col_center, scaleFactor)

backcopy(i)
row_center    = 330
col_center = 500
scaleFactor = 0.12
#my_video.flip_hor("sbcar", row_center, col_center)
#my_video.move_sprite("sbcar", -20, 80)
my_video.scale_sprite("sbcar", row_center, col_center, scaleFactor)


backcopy(i)

row_center    = 340
col_center = 725
scaleFactor = 0.12
#my_video.flip_hor("sbcar", row_center, col_center)
#my_video.move_sprite("sbcar", 10, 275)
my_video.scale_sprite("sbcar", row_center, col_center, scaleFactor)


my_video.show_last_frame()  # You can see the frame


################################################
# Draw the video path:
#my_video.draw_path("fix it felix")
my_video.draw_path("fix it felix")
my_video.draw_path("sbcar")

################################################

# TSP material
the_path = my_video.get_path("sbcar")
my_TSP = TSP(the_path)
my_TSP.best_tour()

the_path = my_video.get_path("fix it felix")
my_TSP = TSP(the_path)
my_TSP.best_tour()
################################################
my_video.play_video(0.5)






