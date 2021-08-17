# AOLME2 classes and functions that we will be demonstrating:
from aolme2 import vid, spr, load_img, plot_img, clean

# Constructor for video class
videoName = "Video1"
num_of_rows = 500
num_of_cols = 700
my_video = vid(videoName, num_of_rows, num_of_cols)

# Add a background image to the video
back = load_img("backgroundMario.JPG") # Background image file
my_video.set_back('back1', back)       # Save it in the video
my_video.show_back('back1')            # Show it

# Create the first video frame
left_offset = 50
top_offset  = 100
my_video.init_video('back1', left_offset, top_offset)  # First video frame
my_video.show_last_frame()             # You can see the frame


my_sprite = spr()          # Construct a sprite
my_sprite.set_sprite("B1") # Load it from the file B1.pickle
my_sprite.show("B1")

# Make the sprite available to your video:
my_sprite_name = "Bowser"
my_video.set_sprite(my_sprite_name, my_sprite)

# Challenge: Prepare a double for-loop 
# to copy the sprite in different positions.
row_center    = 100
column_center = 100
my_video.place_sprite(my_sprite_name, row_center, column_center)


# Show the placed Sprite
my_video.show_last_frame()

# Show Video object information
print(" ")
print("Video Contents")
print(my_video)
print(" ")


print("Challenge: Reproduce the following image")
img = load_img('resultPlaceSpriteExample1.png')
plot_img(img,"Example result")
