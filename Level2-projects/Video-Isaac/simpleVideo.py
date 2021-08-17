import cv2     # CV2 library
import aolme2  # aolme2 library

# Initialize the sprite
my_sprite = aolme2.spr()
my_sprite.set_sprite("B1")


# Read an image from disk
FileName = 'testPlace.png'
img =cv2.imread(FileName)  # Read a file from the disk.
aolme2.plot_img(ExampleImage,"Image Example")


# Init video
bac=cv2.imread("backgroundMario.JPG")

my_video = aolme2.vid('Clock tutorial',500,700)
my_video.set_back('back1',bac)
my_video.init_video('back1', 0, 0)

my_video.set_sprite('B1',my_sprite)


# Place command
my_video.place_sprite('B1',200,200)


# Show last frame
my_video.show_last_frame()