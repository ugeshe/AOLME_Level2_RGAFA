# AOLME2 classes and functions that we will be demonstrating:
from aolme2 import vid, spr, load_img, plot_img, clean, TSP, img_fill

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
my_video.show_back('back1')                 # Show it


# Add a SECOND BACKGROUND 
img = load_img("backgroundCastle.png") # Background image file

# Add the challenges to the image in black or red:
black = "000000"
red   = "FF0000"
        
start_row = 300
end_row   = 310
rows = [start_row, end_row]
        
start_col = 200
end_col   = 210
cols = [start_col, end_col]
        
img_fill(img, rows, cols, red)
plot_img(img, "red mark challenge")
        

my_video.set_back('back2', img)        # Save it in the video
my_video.show_back('back2')                   # Show it

##############################################################

# Add a FIRST SPRITE
my_1st_sprite = spr()          # Construct a sprite
my_1st_sprite.set_sprite("B1") # Load it from the file B1.pickle
my_1st_sprite.show("B1")       # Show it


# Add a SECOND SPRITE
my_2nd_sprite = spr()             # Construct a sprite
my_2nd_sprite.set_sprite("mario") # Load it from the file B1.pickle
my_2nd_sprite.show("mario")       # Show it


##############################################################

# Make the FIRST sprite available to your video:
my_sprite_name_1 = "Bowser"
my_video.set_sprite(my_sprite_name_1, my_1st_sprite)

# Make the SECOND sprite available to your video:
my_sprite_name_2 = "SuperMario"
my_video.set_sprite(my_sprite_name_2, my_2nd_sprite)


###############################################################

# Take a look at what your video knows
print(" ")
print("Video Object Information:")
print(my_video)


##############################################################

# Create the first video frame with FIRST BACKGROUND
left_offset = 120
top_offset  = 50
my_video.init_video('back1', top_offset, left_offset)  # First video frame

# Place the SECOND SPRITE
row_center    = 400
column_center = 100
my_video.place_sprite(my_sprite_name_2, row_center, column_center)


my_video.show_last_frame()  # You can see the frame


####################################################

# Create the second video frame

### Change background and create a new frame:
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


###################################################
### Change background and create a new frame:
left_offset = 20
top_offset  = 130
my_video.set_new_frame('back2', top_offset, left_offset) 

# Replace the bowser with super Mario
row_bowser, col_bowser = my_video.get_sprite_loc("Bowser")
my_video.place_sprite("SuperMario", row_bowser, col_bowser)


################################################
## Make SuperMario rotate, grow, and move

# Rotate Mario
row, col = my_video.get_sprite_loc("SuperMario")
for ang in range(0, 360, 10):
    my_video.set_new_frame('back2', top_offset, left_offset) 
    my_video.rotate_sprite("SuperMario", row, col, ang)

# Grow Mario
sc = 1.0
for scalings in range(1,4,1):
    my_video.set_new_frame('back2', top_offset, left_offset) 
    my_video.scale_sprite("SuperMario", row, col, sc)
    sc += 0.125

# Move Mario
for moves in range(1,4,1):
    my_video.set_new_frame('back2', top_offset, left_offset) 
    my_video.move_sprite("SuperMario", 10, 0)

################################################
# Draw the video path:
my_video.draw_path("SuperMario")

################################################
# TSP material
the_path = my_video.get_path("SuperMario")
my_TSP = TSP(the_path)
my_TSP.best_tour()

################################################
my_video.play_video(0.2)

