# AOLME2 classes and functions that we will be demonstrating:
from aolme2 import vid, spr, load_img, plot_img, clean

# Close all of the old figures.
clean()

# Create a sprite from an external file:
sprite_face = spr()
sprite_face.set_sprite("face")

# Load a background image
backWhite = load_img("backWhite.jpg")

# Initialize the video and place the background frame:
num_of_rows = 576
num_of_cols = 1024
my_video = vid('Example 1', num_of_rows, num_of_cols)
my_video.set_back('back2', backWhite)

row_offset = 0
col_offset = 0
my_video.init_video('back2', row_offset, col_offset)


# Save the sprite in the video.
my_video.set_sprite('face',sprite_face)

# Fix the parameters to the commands given below:
row_center    = 200
column_center = 830
my_video.place_sprite('face', row_center, column_center)

#row_center = 200
#col_center = 200
#my_video.flip_ver('face', row_center, col_center)
#
#row_center = 380
#col_center = 530
#my_video.flip_hor('face', row_center, col_center)


# Show last frame
my_video.show_last_frame()

# Challenge
print("Can you produce the following challenge image?")
Challenge_img = load_img ('ResultFlipExample.png')
plot_img (Challenge_img, "Example result")


