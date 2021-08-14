# AOLME2 classes and functions that we will be demonstrating:
from aolme2 import img_resize, vid, spr, load_img, plot_img, clean, TSP, img_fill
from cv2 import imwrite

# Use reset in IPython to clean up the variables.
# Clean() closes all of the Windows.
clean()
#resize the cure
img = load_img("Antidote.png")
img = img_resize(img, 0.1)
imwrite("TheCure.png",img)

#resize bad guy 1
img2 = load_img("capBoy.jpg")
img2 = img_resize(img2, 0.15)
imwrite("badCapBoy.jpg",img2)

#resize bad lady
img3 = load_img("shortHair.jpg")
img3 = img_resize(img3, 0.15)
imwrite("shortHairGirl.jpg",img3)

#resize bad boss
img4 = load_img("badBoss.jpg")
img4 = img_resize(img4, 0.15)
imwrite("BadBoss.png",img4)

####################################################
# Constructor for video class
videoName = "The cure"
num_of_rows = 850
num_of_cols = 1200
my_video = vid(videoName, num_of_rows, num_of_cols)
####################################################


####################################################
# Add a FIRST BACKGROUND 
theforest = load_img("forest.JPG") # Background image file
my_video.set_back('back1', theforest)       # Save it in the video
my_video.show_back('back1')                 # Show it

# Add a SECOND BACKGROUND 
outerspace = load_img("space.jpg") # Background image filey
my_video.set_back('back2', outerspace)    
####################################################


####################################################
# Add a FIRST SPRITE
Antidote = spr()          # Construct a sprite
Antidote.set_sprite("TheCure")

# Add a SECOND SPRITE
badguy1 = spr()          # Construct a sprite
badguy1.set_sprite("badCapBoy") 

# Add a THIRD SPRITE
badlady2 = spr()          # Construct a sprite
badlady2.set_sprite("shortHairGirl")    

# Add a FOURTH SPRITE
goodgirl = spr()          # Construct a sprite
goodgirl.set_sprite("people") 

# Add a Fifth SPRITE
goodgirl2 = spr()          # Construct a sprite
goodgirl2.set_sprite("people2")

# Add a sixth SPRITE
blackhole = spr()          # Construct a sprite
blackhole.set_sprite("blackhole")

#Add a seventh sprite
badBoss = spr()
badBoss.set_sprite("BadBoss")
####################################################


####################################################
# Make the FIRST sprite available to your video:
antidote = "Antidote"
my_video.set_sprite(antidote, Antidote)

# Make the SECOND sprite available to your video:
badguy= "badguy"
my_video.set_sprite(badguy, badguy1)

# Make the third sprite available to your video:
badlady = "badlady"
my_video.set_sprite(badlady, badlady2)

# Make the fourth sprite available to your video:
goodgirl1 = "goodgirl1"
my_video.set_sprite(goodgirl1, goodgirl)

#Make the FIFTH sprite available to your video:
goodlady = "goodgirl2"
my_video.set_sprite(goodlady, goodgirl2)

## Make the SIXTH sprite available to your video:
blkhole = "blackhole"
my_video.set_sprite(blkhole, blackhole)

# Make the SEVENTH sprite available to your video:
badboss = "badboss"
my_video.set_sprite(badboss,badBoss)
###############################################################


####################################################
# Take a look at what your video knows
print(" ")
print("Video Object Information:")
print(my_video)
##############################################################

# Create the first video frame with FIRST BACKGROUND: FOREST
left_offset = 0
top_offset  = 0
my_video.init_video('back1', top_offset, left_offset)  # First video frame

# Here's an example of how to add or place the first bad girl onto the video.
# Notice that this bad girl will not move, shrink, grow, or rotate.
# The PLACE_SPRITE method only need the location of the bad girl's center, then
#     it can draw the girl for you on the video.
#     Here, I put her at row 750 and col 600

# Place the badlady SPRITE
second_bad_row_center = 750
second_bad_col_center = 600
my_video.place_sprite(badlady, second_bad_row_center, second_bad_col_center)


#Now can you try to find the location of the center for the second bad guy?
# Place the badguy SPRITE

first_bad_row_center = 750
first_bad_col_center = 800
my_video.place_sprite(badguy, first_bad_row_center, first_bad_col_center)


# Place the badboss SPRITE
# How about the boss and the 2 good girls? Now you don't have the code for it,
#    but it should be very similar right? 
# What code do you need to copy?
# HINT: The code you need only has 3 lines for each sprite/object.

# Put the Code for the Bad Boss 
first_badboss_row_center = 750
first_badboss_col_center = 700
my_video.place_sprite(badboss, first_badboss_row_center, first_badboss_col_center)

# Put the code for Good girl 1 original location here
first_goodperson1_row_center = 720
first_goodperson1_col_center = 170
my_video.place_sprite(goodgirl1, first_goodperson1_row_center, first_goodperson1_col_center)


# Put the code for Good girl 2 original location here
first_goodperson2_row_center = 720
first_goodperson2_col_center = 130
my_video.place_sprite(goodlady, first_goodperson2_row_center, first_goodperson2_col_center)

# For Black hole, you would need to find the scale right?
# Last time, we chose it to be 0.1, so each time it will grow a tenth of the 
#    previous size.
# The black hole will also need the location. Can you find it using the picture?
# Do you see what changed compared to the codes for the people?
# HINT: There's a line missing... 
# The reason why we don't have that line is because the black hole and the cure
#    have some special missions to do? You know what it does??


# Black hole sprite original location

blkhole_scaleFactor = 0.1
blk_hole_row_center = 250
blk_hole_col_center = 1000
  

# Fill in the cure location here as well. 
# The cure original location

bottle_row_center = 780
bottle_col_center = 730


# What does for loop do?
# How many times will it repeat?
# What background will the for loop happen?
# FOR LOOP STARTS HERE.
for ang in range(0, 360, 10):
    
    # WHAT does this line do? And why do we need it?
    # Do you think the video would work without it??
    # Why are the offsets 0? 
    # HINT: What is the size of the background? 
    my_video.set_new_frame('back1', top_offset, left_offset) 
    
   # my_video.scale_sprite(badlady, second_bad_row_center-300, second_bad_col_center,1.3)

    
    #black hole
    #If you want the black hole to grow, we need to scale it right?
    #Do you remember the code? If not, open SCALINGEXAMPLE.PY and copy the code.
    # PUT SCALING CODE HERE
    my_video.scale_sprite('blackhole', blk_hole_row_center, blk_hole_col_center,blkhole_scaleFactor)
    #Now we need to tell the computer how much you want it to grow each time right?
    #The for loop repeats the same thing over and over until it's done. 
    #So, if we don't tell the computer to change the scale of the black hole, 
    #   the black hole will not grow.
    #HINT: How much do you want to increase the black hole each time?
    #      If you don't remember, go back up, we talked about it already.
    
    blkhole_scaleFactor = blkhole_scaleFactor + 0.1
  
    #antidote
    #Now, for the cure, what do you want to do with it?
    #Remember the code for this? If not, open exampleRotation1.py and copy code    
    #Copy the code line and put it here
    my_video.rotate_sprite(antidote, bottle_row_center, bottle_col_center, ang)
    #Now, similar to the black hole scaling, you want the cure to rotate multiple
    #   times and move towards the black hole at the same time, right?
    #To do that, you'd need to change its location. You know that you wanna
    #   rotate and move it to the black hole, what direction do you want?
    #  LEFT, RIGHT, UP, or DOWN? And remember which way will be + and which will
    #    be -. Try putting numbers and see what happens :)
    
    bottle_row_center = bottle_row_center -9
    bottle_col_center = bottle_col_center +6
    
    
    # Now, for the bad people, you do not want to move them. 
    # The line of code: my_video.move_sprite has 3 arguments inside the parenthesis
    #   (), the first one is the name of the sprite,
    #   the second one is the amount of rows you want to move (-up or +down)
    #   the third one is the amount of columns you want to move(-left or +right)
    # For ex, if I want the first bad guy to move 10 up and 5 right, the code is:
    #    my_video.move_sprite("badguy",-10,5).
    # Can you fill it in for the first one?
    #    HINT: The bad guys DO NOT move.
    #bad guy
    my_video.move_sprite("badguy",0 ,0 )
    
    
    
    #Can you finish the rest of the bad guys?
    #bad lady
    #Copy the code, put it here, and fill it out.
    my_video.move_sprite("badlady",0 ,0 )
    
    #bad boss
    #Copy the code, put it here, and fill it out.
    my_video.move_sprite("badboss",0 ,0 )

    # HOW ABOUT THE 2 GOOD GIRLS?
    # You still want to move them, so the code should be the same
    # But you do want to move them into the black hole as well right?
    # So the row and column will be different. Give it a try.
    #good girl 1

    my_video.move_sprite("goodgirl1",-10,20)
    
    #good girl 2
    #Copy the code, put it here, and fill it out.
    my_video.move_sprite("goodgirl2",-10,20)
    


#################################################
### Draw the video path:
my_video.draw_path("goodgirl1")
#my_video.draw_path("badlady")
##
###
###################################################
##### TSP material
#the_path = my_video.get_path("goodgirl1")
##the_path = my_video.get_path("badlady")
###
#my_TSP = TSP(the_path)
#my_TSP.best_tour()
#################################################
my_video.show_last_frame()  # You can see the frame
my_video.play_video(0.08) 