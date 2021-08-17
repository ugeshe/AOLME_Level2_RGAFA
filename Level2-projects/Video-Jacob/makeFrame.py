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
left_offset = 500
top_offset  = 100
my_video.init_video('back1', left_offset, top_offset)  # First video frame
my_video.show_last_frame()             # You can see the frame
