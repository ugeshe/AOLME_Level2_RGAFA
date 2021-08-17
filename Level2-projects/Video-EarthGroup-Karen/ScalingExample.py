# AOLME2 classes and functions that we will be demonstrating:
from aolme2 import vid, spr, load_img, plot_img, clean


# Init example sprite
my_sprite = spr()
my_sprite.set_sprite("B1")

# Init video
bac = load_img("backgroundMario.JPG")

my_video = vid('Scaling Challenge',560,900)
my_video.set_back('back1',bac)
my_video.init_video('back1', 0, 100)

my_video.set_sprite('B1',my_sprite)


######## Fix the scale_sprite() commands below ########
# After you figure out the parameters, try solving 
# the problem using a for-loop
scaleFactor=1
row_center = 300
col_center = 100
my_video.scale_sprite('B1', row_center, col_center,scaleFactor)

# Show last frame
my_video.show_last_frame() 

print("Scaling challenge: produce this image")
scale_challenge = load_img("resultScalingExample.png")
plot_img(scale_challenge, "Scale Challenge")
   





