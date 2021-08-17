from aolme2 import vid, spr, load_img, plot_img, clean

# Close all of the figures
clean()

# Read the puppy sprite from Puppy.pickle.
my_sprite = spr()
my_sprite.set_sprite("Puppy")

# Read the background image
bac=load_img("bg_wall_1.png")
video_rows=bac.shape[0]  # number of rows.
video_cols=bac.shape[1]  # number of columns.

# Init video
my_video = vid('TSP Puppy',video_rows,video_cols)
my_video.set_back('house',bac)
my_video.init_video('house', 0, 0)

# Set sprite inside "my_video"
my_video.set_sprite('puppy',my_sprite)


######## Starting point for the puppy ########
start_row = 250
start_col = 250
my_video.place_sprite('puppy',start_row,start_col)


# Second frame 
rows_move = 0
cols_move = 400
my_video.set_new_frame('house',0,0)
my_video.move_sprite('puppy',rows_move,cols_move,Trace=True)


# Third frame
rows_move = 250
cols_move = 200
my_video.set_new_frame('house',0,0)
my_video.move_sprite('puppy',rows_move,cols_move,Trace=True)


# Third frame 
rows_move = -30
cols_move = -380
my_video.set_new_frame('house',0,0)
my_video.move_sprite('puppy',rows_move,cols_move,Trace=True)



my_video.draw_path('puppy')

print(" ")
print(my_video)
print(" ")

delay_between_frames = 1 # in seconds
my_video.play_video(delay_between_frames)
