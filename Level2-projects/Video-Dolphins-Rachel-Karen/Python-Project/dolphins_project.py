# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 09:24:34 2018

@author: AOLME_SnowWhite_1
"""

# AOLME2 classes and functions that we will be demonstrating:
from aolme2 import vid, spr, load_img, plot_img, clean, img_fill, TSP

# Use reset in IPython to clean up the variables.
# Clean() closes all of the Windows.
clean()

# Constructor for video class
videoName = "food"
num_of_rows = 426
num_of_cols = 626
my_video = vid(videoName, num_of_rows, num_of_cols)

##############################################################

# Add a FIRST BACKGROUND 
backfarm = load_img("farm_bg.JPG") # Background image file
my_video.set_back('farm', backfarm)       # Save it in the video
my_video.show_back('farm')                 # Show it


 # Add a FIRST SPRITE
my_seahorse_sprite = spr()          # Construct a sprite
my_seahorse_sprite.set_sprite("happy_seahorse") # Load it from the file B1.pickle
my_seahorse_sprite.show("happy_seahorse")

# Add second sprite
my_puppy_sprite = spr()          # Construct a sprite
my_puppy_sprite.set_sprite("sad_dog") # Load it from the file B1.pickle
my_puppy_sprite.show("sad_dog")   

   # add third sprite
my_sadpig_sprite = spr()          # Construct a sprite
my_sadpig_sprite.set_sprite("sad_pig") # Load it from the file B1.pickle
my_sadpig_sprite.show("sad_pig")   

    # Add a Fourth SPRITE
my_sadcat_sprite = spr ()         # Construct a sprite
my_sadcat_sprite.set_sprite("sad_cat") # Load it from the file B1.pickle
my_sadcat_sprite.show("sad_cat")

    # Add a Fifth SPRITE
my_potato_sprite = spr ()         # Construct a sprite
my_potato_sprite.set_sprite("potato") # Load it from the file B1.pickle
my_potato_sprite.show("potato")

# Add sixth sprite
my_potatoarmy_sprite = spr()          # Construct a sprite
my_potatoarmy_sprite.set_sprite("potato_army") # Load it from the file B1.pickle
my_potatoarmy_sprite.show("potato_army")   

# Add seventh sprite
my_happypig_sprite = spr()          # Construct a sprite
my_happypig_sprite.set_sprite("happy_pig") # Load it from the file B1.pickle
my_happypig_sprite.show("happy_pig")  

    # Add a eigth SPRITE
my_happycat_sprite = spr ()         # Construct a sprite
my_happycat_sprite.set_sprite("happy_cat") # Load it from the file B1.pickle
my_happycat_sprite.show("happy_cat")

# Add ninth sprite
my_happypuppy_sprite = spr()          # Construct a sprite
my_happypuppy_sprite.set_sprite("happy_dog") # Load it from the file B1.pickle
my_happypuppy_sprite.show("happy_dog")   

# Add tenth sprite
my_smoke_sprite = spr()          # Construct a sprite
my_smoke_sprite.set_sprite("smoke") # Load it from the file B1.pickle
my_smoke_sprite.show("smoke")   

# Make the FIRST sprite available to your video:
my_sprite_name_1 = "seahorse"
my_video.set_sprite(my_sprite_name_1, my_seahorse_sprite)

# Make the secondsprite available to your video:
my_sprite_name_2 = "sad_dog"
my_video.set_sprite(my_sprite_name_2, my_puppy_sprite)

# Make the thirdsprite available to your video:
my_sprite_name_3 = "sad_pig"
my_video.set_sprite(my_sprite_name_3, my_sadpig_sprite)

# Make the fourthsprite available to your video:
my_sprite_name_4 = "sad_cat"
my_video.set_sprite(my_sprite_name_4, my_sadcat_sprite)

# Make the fifthsprite available to your video:
my_sprite_name_5 = "potato"
my_video.set_sprite(my_sprite_name_5, my_potato_sprite)

# Make the Sixth sprite available to your video:
my_sprite_name_6 = "potato_army"
my_video.set_sprite(my_sprite_name_6, my_potatoarmy_sprite)

# Make the seventh sprite available to your video:
my_sprite_name_7 = "happy_pig"
my_video.set_sprite(my_sprite_name_7, my_happypig_sprite)

# Make the eighth sprite available to your video:
my_sprite_name_8 = "happy_cat"
my_video.set_sprite(my_sprite_name_8, my_happycat_sprite)

# Make the ninthsprite available to your video:
my_sprite_name_9 = "happy_dog"
my_video.set_sprite(my_sprite_name_9, my_happypuppy_sprite)

# Make the ninthsprite available to your video:
my_sprite_name_10 = "smoke"
my_video.set_sprite(my_sprite_name_10, my_smoke_sprite)
###############################################################################
#FRAME 1
###############################################################################

# Create the first video frame with FIRST BACKGROUND
left_offset = 0
top_offset  = 200
my_video.init_video('farm', top_offset, left_offset)  # First video frame


# Place the first SPRITE
scaleFactor=0.1
row_center    = 250
column_center = 480
my_video.scale_sprite(my_sprite_name_1, row_center, column_center,scaleFactor)


# Place the second SPRITE
scaleFactor=0.2
row_center    = 210
column_center = 240
my_video.scale_sprite(my_sprite_name_2, row_center, column_center,scaleFactor)

# Place the third SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 350
my_video.scale_sprite(my_sprite_name_3, row_center, column_center,scaleFactor)

# place fourth sprite
scaleFactor=0.1
row_center    = 120
column_center = 450
my_video.scale_sprite(my_sprite_name_4, row_center, column_center,scaleFactor)

my_video.show_last_frame()  # You can see the frame 

###############################################################################
#FRAME 2
###############################################################################

#Make new frame
my_video.set_new_frame('farm', top_offset, left_offset)


# Place first SPRITE
scaleFactor=0.1
row_center    = 250
column_center = 480
my_video.scale_sprite(my_sprite_name_1, row_center, column_center,scaleFactor)

# Place second SPRITE
scaleFactor=0.2
row_center    = 210
column_center = 240
my_video.scale_sprite(my_sprite_name_2, row_center, column_center,scaleFactor)

# Place third SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 350
my_video.scale_sprite(my_sprite_name_3, row_center, column_center,scaleFactor)

# place fourth sprite
scaleFactor=0.1
row_center    = 120 
column_center = 450
my_video.scale_sprite(my_sprite_name_4, row_center, column_center,scaleFactor)

# place fifth sprite
scaleFactor=0.05
row_center    = 130
column_center = 225
my_video.scale_sprite(my_sprite_name_5, row_center, column_center,scaleFactor)

###############################################################################
#FRAME 3
###############################################################################

#Make new frame
my_video.set_new_frame('farm', top_offset, left_offset)


# Place first SPRITE
scaleFactor=0.1
row_center    = 250
column_center = 480
my_video.scale_sprite(my_sprite_name_1, row_center, column_center,scaleFactor)

# Place second SPRITE
scaleFactor=0.2
row_center    = 210
column_center = 240
my_video.scale_sprite(my_sprite_name_2, row_center, column_center,scaleFactor)

# Place third SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 350
my_video.scale_sprite(my_sprite_name_3, row_center, column_center,scaleFactor)

# place fourth sprite
scaleFactor=0.1
row_center    = 120 
column_center = 450
my_video.scale_sprite(my_sprite_name_4, row_center, column_center,scaleFactor)

# place fifth sprite
scaleFactor=0.1
row_center    = 150
column_center = 150
my_video.scale_sprite(my_sprite_name_5, row_center, column_center,scaleFactor)

###############################################################################
#FRAME 4
###############################################################################

#Make new frame
my_video.set_new_frame('farm', top_offset, left_offset)


# Place first SPRITE
scaleFactor=0.1
row_center    = 250
column_center = 480
my_video.scale_sprite(my_sprite_name_1, row_center, column_center,scaleFactor)

# Place second SPRITE
scaleFactor=0.2
row_center    = 210
column_center = 240
my_video.scale_sprite(my_sprite_name_2, row_center, column_center,scaleFactor)

# Place third SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 350
my_video.scale_sprite(my_sprite_name_3, row_center, column_center,scaleFactor)

# place fourth sprite
scaleFactor=0.1
row_center    = 120 
column_center = 450
my_video.scale_sprite(my_sprite_name_4, row_center, column_center,scaleFactor)

# place fifth sprite
scaleFactor=0.2
row_center    = 170
column_center = 200
my_video.scale_sprite(my_sprite_name_5, row_center, column_center,scaleFactor)

###############################################################################
#FRAME 5
###############################################################################

#Make new frame
my_video.set_new_frame('farm', top_offset, left_offset)


# Place first SPRITE
scaleFactor=0.1
row_center    = 250
column_center = 480
my_video.scale_sprite(my_sprite_name_1, row_center, column_center,scaleFactor)

# Place second SPRITE
scaleFactor=0.2
row_center    = 210
column_center = 240
my_video.scale_sprite(my_sprite_name_2, row_center, column_center,scaleFactor)

# Place third SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 350
my_video.scale_sprite(my_sprite_name_3, row_center, column_center,scaleFactor)

# place fourth sprite
scaleFactor=0.1
row_center    = 120 
column_center = 450
my_video.scale_sprite(my_sprite_name_4, row_center, column_center,scaleFactor)

# place fifth sprite
scaleFactor=0.3
row_center    = 200
column_center = 300
my_video.scale_sprite(my_sprite_name_5, row_center, column_center,scaleFactor)

###############################################################################
#FRAME 6
###############################################################################

#Make new frame
my_video.set_new_frame('farm', top_offset, left_offset)


# Place first SPRITE
scaleFactor=0.1
row_center    = 250
column_center = 480
my_video.scale_sprite(my_sprite_name_1, row_center, column_center,scaleFactor)

# Place second SPRITE
scaleFactor=0.2
row_center    = 210
column_center = 240
my_video.scale_sprite(my_sprite_name_2, row_center, column_center,scaleFactor)

# Place third SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 350
my_video.scale_sprite(my_sprite_name_3, row_center, column_center,scaleFactor)

# place fourth sprite
scaleFactor=0.1
row_center    = 120 
column_center = 450
my_video.scale_sprite(my_sprite_name_4, row_center, column_center,scaleFactor)

# place fifth sprite
scaleFactor=0.3
row_center    = 200
column_center = 150
my_video.scale_sprite(my_sprite_name_5, row_center, column_center,scaleFactor)

###############################################################################
#FRAME 7
###############################################################################

#Make new frame
my_video.set_new_frame('farm', top_offset, left_offset)


# Place first SPRITE
scaleFactor=0.1
row_center    = 250
column_center = 480
my_video.scale_sprite(my_sprite_name_1, row_center, column_center,scaleFactor)

# Place second SPRITE
scaleFactor=0.2
row_center    = 210
column_center = 240
my_video.scale_sprite(my_sprite_name_2, row_center, column_center,scaleFactor)

# Place third SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 350
my_video.scale_sprite(my_sprite_name_3, row_center, column_center,scaleFactor)

# place fourth sprite
scaleFactor=0.1
row_center    = 120 
column_center = 450
my_video.scale_sprite(my_sprite_name_4, row_center, column_center,scaleFactor)

# place fifth sprite
scaleFactor=0.3
row_center    = 200
column_center = 150
my_video.scale_sprite(my_sprite_name_5, row_center, column_center,scaleFactor)

# place sixth sprite
scaleFactor=0.2
row_center    = 240
column_center = 240
my_video.scale_sprite(my_sprite_name_6, row_center, column_center,scaleFactor)

###############################################################################
#FRAME 8
###############################################################################

#Make new frame
my_video.set_new_frame('farm', top_offset, left_offset)


# Place first SPRITE
scaleFactor=0.1
row_center    = 250
column_center = 480
my_video.scale_sprite(my_sprite_name_1, row_center, column_center,scaleFactor)

# Place ninth SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 240
my_video.scale_sprite(my_sprite_name_9, row_center, column_center,scaleFactor)

# Place third SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 350
my_video.scale_sprite(my_sprite_name_3, row_center, column_center,scaleFactor)

# place fourth sprite
scaleFactor=0.1
row_center    = 120 
column_center = 450
my_video.scale_sprite(my_sprite_name_4, row_center, column_center,scaleFactor)

# place fifth sprite
scaleFactor=0.3
row_center    = 200
column_center = 300
my_video.scale_sprite(my_sprite_name_5, row_center, column_center,scaleFactor)

# place sixth sprite
scaleFactor=0.2
row_center    = 250
column_center = 350
my_video.scale_sprite(my_sprite_name_6, row_center, column_center,scaleFactor)

###############################################################################
#FRAME 9
###############################################################################

#Make new frame
my_video.set_new_frame('farm', top_offset, left_offset)


# Place first SPRITE
scaleFactor=0.1
row_center    = 250
column_center = 480
my_video.scale_sprite(my_sprite_name_1, row_center, column_center,scaleFactor)

# Place ninth SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 240
my_video.scale_sprite(my_sprite_name_9, row_center, column_center,scaleFactor)

# Place seventh SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 350
my_video.scale_sprite(my_sprite_name_7, row_center, column_center,scaleFactor)

# place fourth sprite
scaleFactor=0.1
row_center    = 120 
column_center = 450
my_video.scale_sprite(my_sprite_name_4, row_center, column_center,scaleFactor)

# place fifth sprite
scaleFactor=0.3
row_center    = 190
column_center = 440
my_video.scale_sprite(my_sprite_name_5, row_center, column_center,scaleFactor)

# place sixth sprite
scaleFactor=0.2
row_center    = 260
column_center = 440
my_video.scale_sprite(my_sprite_name_6, row_center, column_center,scaleFactor)


###############################################################################
#FRAME 10
###############################################################################

#Make new frame
my_video.set_new_frame('farm', top_offset, left_offset)


# Place first SPRITE
scaleFactor=0.1
row_center    = 250
column_center = 480
my_video.scale_sprite(my_sprite_name_1, row_center, column_center,scaleFactor)

# Place ninth SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 240
my_video.scale_sprite(my_sprite_name_9, row_center, column_center,scaleFactor)

# Place seventh SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 350
my_video.scale_sprite(my_sprite_name_7, row_center, column_center,scaleFactor)

# place fourth sprite
scaleFactor=0.1
row_center    = 120 
column_center = 450
my_video.scale_sprite(my_sprite_name_4, row_center, column_center,scaleFactor)

# place fifth sprite
scaleFactor=0.2
row_center    = 170
column_center = 420
my_video.scale_sprite(my_sprite_name_5, row_center, column_center,scaleFactor)

# place sixth sprite
scaleFactor=0.1
row_center    = 200
column_center = 440
my_video.scale_sprite(my_sprite_name_6, row_center, column_center,scaleFactor)

###############################################################################
#FRAME 11
###############################################################################

#Make new frame
my_video.set_new_frame('farm', top_offset, left_offset)


# Place first SPRITE
scaleFactor=0.1
row_center    = 250
column_center = 480
my_video.scale_sprite(my_sprite_name_1, row_center, column_center,scaleFactor)

# Place ninth SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 240
my_video.scale_sprite(my_sprite_name_9, row_center, column_center,scaleFactor)

# Place seventh SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 350
my_video.scale_sprite(my_sprite_name_7, row_center, column_center,scaleFactor)

# place eighth sprite
scaleFactor=0.05
row_center    = 120 
column_center = 450
my_video.scale_sprite(my_sprite_name_8, row_center, column_center,scaleFactor)

# place fifth sprite
scaleFactor=0.2
row_center    = 170
column_center = 420
my_video.scale_sprite(my_sprite_name_5, row_center, column_center,scaleFactor)

###############################################################################
#FRAME 12
###############################################################################

#Make new frame
my_video.set_new_frame('farm', top_offset, left_offset)


# Place first SPRITE
scaleFactor=0.1
row_center    = 250
column_center = 480
my_video.scale_sprite(my_sprite_name_1, row_center, column_center,scaleFactor)

# Place ninth SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 240
my_video.scale_sprite(my_sprite_name_9, row_center, column_center,scaleFactor)

# Place seventh SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 350
my_video.scale_sprite(my_sprite_name_7, row_center, column_center,scaleFactor)

# place eighth sprite
scaleFactor=0.05
row_center    = 120 
column_center = 450
my_video.scale_sprite(my_sprite_name_8, row_center, column_center,scaleFactor)

# place fifth sprite
scaleFactor=0.3
row_center    = 200
column_center = 120
my_video.scale_sprite(my_sprite_name_5, row_center, column_center,scaleFactor)

###############################################################################
#FRAME 13
###############################################################################

#Make new frame
my_video.set_new_frame('farm', top_offset, left_offset)


# Place first SPRITE
scaleFactor=0.1
row_center    = 250
column_center = 480
my_video.scale_sprite(my_sprite_name_1, row_center, column_center,scaleFactor)

# Place ninth SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 240
my_video.scale_sprite(my_sprite_name_9, row_center, column_center,scaleFactor)

# Place seventh SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 350
my_video.scale_sprite(my_sprite_name_7, row_center, column_center,scaleFactor)

# place eighth sprite
scaleFactor=0.05
row_center    = 120 
column_center = 450
my_video.scale_sprite(my_sprite_name_8, row_center, column_center,scaleFactor)

# place  tenth sprite
scaleFactor=1
row_center    = 200
column_center = 120
my_video.scale_sprite(my_sprite_name_10, row_center, column_center,scaleFactor)

###############################################################################
#FRAME 14
###############################################################################

#Make new frame
my_video.set_new_frame('farm', top_offset, left_offset)


# Place first SPRITE
scaleFactor=0.1
row_center    = 250
column_center = 480
my_video.scale_sprite(my_sprite_name_1, row_center, column_center,scaleFactor)

# Place ninth SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 240
my_video.scale_sprite(my_sprite_name_9, row_center, column_center,scaleFactor)

# Place seventh SPRITE
scaleFactor=0.1
row_center    = 210
column_center = 350
my_video.scale_sprite(my_sprite_name_7, row_center, column_center,scaleFactor)

# place eighth sprite
scaleFactor=0.05
row_center    = 120 
column_center = 450
my_video.scale_sprite(my_sprite_name_8, row_center, column_center,scaleFactor)

# Draw the video path:
my_video.draw_path("potato")

###############################################
# TSP material
the_path = my_video.get_path("potato")
my_TSP = TSP(the_path)
my_TSP.best_tour()

##############################################################################
#PLAY VIDEO
##############################################################################
my_video.play_video(0.5)