# AOLME2 classes and functions that we will be demonstrating:
from aolme2 import vid, spr, load_img, plot_img, clean

# Create a sprite from the clock image
my_sprite = spr()              # Constructor
my_sprite.set_sprite("clock")  # Read the clock sprite
my_sprite.show("Clock sprite")

# Read the wall image for background
back1 = load_img("wall.jpg")

# Initialize the video
num_of_rows = 850
num_of_cols = 850
my_video    = vid('Rotation Example 1', num_of_rows, num_of_cols)

# Add the background to the video
my_video.set_back('wall', back1)

# Make the first frame at the top-left portion of the background
my_video.init_video('wall', 0, 0)

# Add the sprite to the video
spr_name = 'clock'
my_video.set_sprite('clock',my_sprite)


# Place a rotated copy of the sprite on the frame
angle = 0         # angle in degrees
row_center = 200
col_center = 200
my_video.rotate_sprite(spr_name, row_center, col_center, angle)

# Look at the rotated image    
my_video.show_last_frame()
    
    

# Display the challenge
print("Can you produce the last figure using rotate_sprite()?")
Challenge_img=load_img('resultRotation1.png')
plot_img(Challenge_img,"Rotation Challenge")
