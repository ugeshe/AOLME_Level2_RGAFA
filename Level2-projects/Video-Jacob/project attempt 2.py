# AOLME2 classes and functions that we will be demonstrating:
from aolme2 import vid, spr, load_img, plot_img, clean, TSP, img_fill

# Use reset in IPython to clean up the variables.
# Clean() closes all of the Windows.
clean()

# Constructor for video class
videoName = "Video1"
num_of_rows = 800
num_of_cols = 1000
my_video = vid(videoName, num_of_rows, num_of_cols)


##############################################################

# Add a FIRST BACKGROUND 
backtilt = load_img("tilted background.JPG") # Background image file
my_video.set_back('back1', backtilt)        # Save it in the video
my_video.show_back('back1')                 # Show it

backtilt2 = load_img("metalwall.jpg")       # Background image file
my_video.set_back('back2', backtilt2)       # Save it in the video
my_video.show_back('back2')                 # Show it



#Initialize video
left_offset = 100
top_offset  = 100
my_video.init_video('back1', top_offset, left_offset)  # First vid

# Add a FIRST SPRITE (ghould trooper)
my_1st_sprite = spr()                     # Construct a sprite
my_1st_sprite.set_sprite("ghoul trooper") # Load it from the file -pickle
my_1st_sprite.show("ghoul trooper")       # Show it
my_sprite_name_1 = "ghoul trooper"        
my_video.set_sprite(my_sprite_name_1, my_1st_sprite) #Make sprite available


# Add a second SPRITE  (chug jug)
my_2nd_sprite = spr()                # Construct a sprite
my_2nd_sprite.set_sprite("chug jug") # Load it from the file pickle
my_2nd_sprite.show("chug jug")       # Show it
my_sprite_name_2 = "chug jug"        # Adding the sprite to the video
my_video.set_sprite(my_sprite_name_2, my_2nd_sprite) #Make it availible


# Add a third SPRITE (knocked player)
my_3rd_sprite = spr()          # Construct a sprite
my_3rd_sprite.set_sprite("knocked fortnite player") # Load it from the file pickle
my_3rd_sprite.show("knocked fortnite player")  
my_sprite_name_3 = "knocked fortnite player"        # Adding the sprite to the video
my_video.set_sprite(my_sprite_name_3, my_3rd_sprite)

# Add another (porta fort ball
my_4th_sprite = spr()          # Construct a sprite
my_4th_sprite.set_sprite("porta fort ball") # Load it from the file pickle
my_4th_sprite.show("porta fort ball")  
my_sprite_name_4 = "porta fort ball"        # Adding the sprite to the video
my_video.set_sprite(my_sprite_name_4, my_4th_sprite)

my_5th_sprite = spr()          # Construct a sprite
my_5th_sprite.set_sprite("porta fort") # Load it from the file pickle
my_5th_sprite.show("porta fort")  
my_sprite_name_5 = "porta fort"        # Adding the sprite to the video
my_video.set_sprite(my_sprite_name_5, my_5th_sprite)

#adding latter sprite
my_6th_sprite = spr()          # Construct a sprite
my_6th_sprite.set_sprite("woodlatter") # Load it from the file pickle
my_6th_sprite.show("woodlatter")  
my_sprite_name_6 = "woodlatter"        # Adding the sprite to the video
my_video.set_sprite(my_sprite_name_6, my_6th_sprite)

# Take a look at what your video knows
print(" ")
print("Video Object Information:")
print(my_video)

###########################################
#1st frame ghoul moving toward knocked player
##############################################
row = 700       #ghoul trooper
col = 100
sc = 1 #sizing the ghoul trooper 
my_video.scale_sprite("ghoul trooper", row, col, sc)    

#knocked player location
row_center2    = 700 
column_center2 = 800
my_video.place_sprite(my_sprite_name_3, row_center2, column_center2)

 
# For loop making the ghoul trooper move

for moves in range(1,4,1):
    my_video.set_new_frame('back1', 100, 100) 
    my_video.move_sprite("ghoul trooper", -200, 200)
    my_video.place_sprite(my_sprite_name_3, row_center2, column_center2)
    my_video.flip_hor('woodlatter',600,470)
    my_video.flip_hor('woodlatter',500,550)
    my_video.flip_hor('woodlatter',400,650)
    my_video.flip_hor('woodlatter',300,750)
    
#########################################
# Throwin' down tha portafort
#########################################    
my_video.set_new_frame('back1', 100, 100)     


my_video.place_sprite(my_sprite_name_3, 700, 800)
my_video.scale_sprite("ghoul trooper", 700, 700, sc)  
row_center    = 700
column_center = 400
 # adding the porta forta ball
row3 = 700       
col3 = 700
sc = .1                         #sizing the porta fort ball
my_video.scale_sprite("porta fort ball", row3, col3, sc)    

##########################################
# adding new frame, growing the porta fort
###########################################
my_video.set_new_frame('back1', 100, 100) 

my_video.place_sprite(my_sprite_name_5, 500, 500)

# Grow porta fort
sc = 1.0
for scalings in range(1,6,1):
    my_video.set_new_frame('back1', 0, 0) 
    my_video.scale_sprite("porta fort", 500, 500, sc)
    sc += 0.15
#########################    
#final frame
###########################
my_video.set_new_frame('back2', 100, 100)
#ghoul trooper
row = 700       
col = 200
sc = 1 #sizing the ghoul trooper 
my_video.scale_sprite("ghoul trooper", row, col, sc)    

#knocked player location
row_center2    = 700 
column_center2 = 800
my_video.place_sprite(my_sprite_name_3, row_center2, column_center2)

sc = .25 #sizing the chug jug 
my_video.scale_sprite("chug jug", row, col, sc)
row = 700
col = 250
# For looop making the frames move
for moves in range(1,4,1):
    col = col+200
    my_video.set_new_frame('back2', 100, 100) 
    my_video.move_sprite("ghoul trooper", 0, 200)
    my_video.place_sprite(my_sprite_name_3, row_center2, column_center2)
    my_video.scale_sprite("chug jug", row, col, sc)

# END VIDEO

################################################
# Draw the video path:
my_video.draw_path("ghoul trooper")

################################################
# TSP material
the_path = my_video.get_path("ghoul trooper")
my_TSP = TSP(the_path)
my_TSP.best_tour()

################################################


my_video.show_last_frame() 
my_video.play_video(0.2)