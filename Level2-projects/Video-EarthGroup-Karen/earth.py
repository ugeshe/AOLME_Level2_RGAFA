
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 12:17:06 2018

@author: Aolme6
"""
# AOLME2 classes and functions that we will be demonstrating:
from aolme2 import vid, spr, load_img, plot_img, clean, img_fill, TSP, img_resize

# Use reset in IPython to clean up the variables.
# Clean() closes all of the Windows.
clean()

# Constructor for video class
videoName = "Video1"
num_of_rows = 1200
num_of_cols = 1600
my_video = vid(videoName, num_of_rows, num_of_cols)


def place_all():
    row=100
    col=1300
    sc=0.1
    my_video.scale_sprite(shark2, row, col, sc)
    
    row=400
    col=250
    sc=1.5
    my_video.scale_sprite(cage, row, col, sc)
   
    row=200
    col=600
    sc=1.0
    my_video.scale_sprite(turtle, row, col, sc)

    row=200
    col=600
    sc=1.5
    my_video.scale_sprite(plastic_bag, row, col, sc)
 
    
##############################################################

# Add a FIRST BACKGROUND 
img = load_img("ocean.jpg") # Background image file
backocean = img_resize(img, 5)
my_video.set_back('ocean', backocean)       # Save it in the video
my_video.show_back('ocean')                 # Show it

##############################################################

# Add a FIRST SPRITE
spr1 = spr()          # Construct a sprite
spr1.set_sprite("dolphin") # Load it from the file B1.pickle
spr1.show("dolphin")       # Show it


# Add a SECOND SPRITE
spr2 = spr()             # Construct a sprite
spr2.set_sprite("shark1") # Load it from the file B1.pickle
spr2.show("shark1")       # Show it


# Add a THIRD SPRITE
spr3 = spr()             # Construct a sprite
spr3.set_sprite("shark2") # Load it from the file B1.pickle
spr3.show("shark2")       # Show it


# Add a FOURTH SPRITE
spr4 = spr()             # Construct a sprite
spr4.set_sprite("octopus") # Load it from the file B1.pickle
spr4.show("octopus")       # Show it

# Add a FIFTH SPRITE
spr5 = spr()             # Construct a sprite
spr5.set_sprite("turtle") # Load it from the file B1.pickle
spr5.show("turtle")       # Show it


  


# Add a NINETH SPRITE
spr9 = spr()             # Construct a sprite
spr9.set_sprite("cage") # Load it from the file B1.pickle
spr9.show("cage")       # Show it


# Add a TENTH SPRITE
spr10 = spr()             # Construct a sprite
spr10.set_sprite("plastic_bag") # Load it from the file B1.pickle
spr10.show("plastic_bag")       # Show it

# Sprites get associated with video
dolphin = "dolphin"
my_video.set_sprite(dolphin, spr1)

print(my_video)


shark2 = "shark2"
my_video.set_sprite(shark2, spr3)

print(my_video)


shark1 = "shark1"
my_video.set_sprite(shark1, spr2)

print(my_video)


turtle = "turtle"
my_video.set_sprite(turtle, spr5)

print(my_video)




cage = "cage"
my_video.set_sprite(cage, spr9)

print(my_video)


plastic_bag = "plastic_bag"
my_video.set_sprite(plastic_bag, spr10)

print(my_video)


octopus = "octopus"
my_video.set_sprite(octopus, spr4)

print(my_video)





# Create the first video frame with FIRST BACKGROUND (trash1)


#shark1 sprite
left_offset = 0
top_offset  = 0
my_video.init_video('ocean', top_offset, left_offset)  # First video frame

place_all()
row=400
col=850
sc = 1
my_video.scale_sprite('dolphin', row, col, sc)

scol=400
srow=700
sc=0.4
my_video.scale_sprite(shark1, srow, scol, sc)
    
orow=800
ocol=1000
sc=0.5
my_video.scale_sprite(octopus, orow, ocol, sc)
#
##dolphin sprite
#left_offset = 0
#top_offset  = 0
#my_video.init_video('ocean', top_offset, left_offset)  # First video frame



#my_video.set_new_frame('ocean', top_offset, left_offset) 

print(my_video)

srow=700
scol=400

drow=400
dcol=850
for i in range(28):
    my_video.set_new_frame('ocean', 0,0)
    place_all()
    sc = 1
    dcol=dcol-20
    my_video.scale_sprite('dolphin', drow, dcol, sc)
    
    scol=scol+5
    sc=0.4
    my_video.scale_sprite(shark1, srow, scol, sc)
    
    orow=orow-15
    ocol=ocol-18
    sc=0.5
    my_video.scale_sprite(octopus, orow, ocol, sc)

    
    


my_video.play_video(0.5)

