# AOLME2 classes and functions that we will be demonstrating:
from aolme2 import vid, spr, load_img, plot_img, clean

# Constructor for video class
videoName = "Video1"
num_of_rows = 500
num_of_cols = 700
my_video = vid(videoName, num_of_rows, num_of_cols)

# Add a background image to the video
background = load_img("backgroundMario.JPG") # Background image file
my_video.set_back('back1', background)       # Save it in the video
my_video.show_back('back1')            # Show it

# Create the first video frame
left_offset = 400
top_offset  = 00000
-+..........

my_video.init_video('back1',top_offset,left_offset)  # First video frame
my_video.show_last_frame()             # You can see the frame
