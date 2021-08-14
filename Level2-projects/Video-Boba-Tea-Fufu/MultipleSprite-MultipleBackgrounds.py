# AOLME2 classes and functions that we will be demonstrating:
from aolme2 import vid, spr, load_img, plot_img, clean

# Use reset in IPython to clean up the variables.
# Clean() closes all of the Windows.
clean()

# Constructor for video class
videoName = "Video1"
num_of_rows = 500
num_of_cols = 700
my_video = vid(videoName, num_of_rows, num_of_cols)

##############################################################

# Add a FIRST BACKGROUND 
backMario = load_img("backgroundMario.JPG") # Background image file
my_video.set_back('back1', backMario)       # Save it in the video
my_video.show_back('back1') # Show it


# Add a SECOND BACKGROUND 
backCastle = load_img("backgroundCastle.png") # Background image file
my_video.set_back('back2', backCastle)       # Save it in the video
my_video.show_back('back2') # Show it

##############################################################

# Add a FIRST SPRITE
my_1st_sprite = spr()          # Construct a sprite
my_1st_sprite.set_sprite("B1") # Load it from the file B1.pickle
my_1st_sprite.show("B1")


# Add a SECOND SPRITE
my_2nd_sprite = spr()          # Construct a sprite
my_2nd_sprite.set_sprite("mario") # Load it from the file B1.pickle
my_2nd_sprite.show("mario")

##############################################################

# Make the FIRST sprite available to your video:
my_sprite_name_1 = "Bowser"
my_video.set_sprite(my_sprite_name_1, my_1st_sprite)

# Make the SECOND sprite available to your video:
my_sprite_name_2 = "SuperMario"
my_video.set_sprite(my_sprite_name_2, my_2nd_sprite)


##############################################################

# Create the first video frame with FIRST BACKGROUND
left_offset = 120
top_offset  = 50
my_video.init_video('back1', top_offset, left_offset)  # First video frame

# Place the SECOND SPRITE
row_center    = 400
column_center = 100
my_video.place_sprite(my_sprite_name_2, row_center, column_center)


my_video.show_last_frame()             # You can see the frame

### Change background
left_offset = 20
top_offset  = 130
my_video.set_new_frame('back2', top_offset, left_offset) 


# Place the SECOND SPRITE
row_center    = 300
column_center = 200
my_video.place_sprite(my_sprite_name_2, row_center, column_center)

# Place the FIRST SPRITE
row_center    = 140
column_center = 500
my_video.place_sprite(my_sprite_name_1, row_center, column_center)


my_video.show_last_frame()             # You can see the frame

my_video.play_video(1)
