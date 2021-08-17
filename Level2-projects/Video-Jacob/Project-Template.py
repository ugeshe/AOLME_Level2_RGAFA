# AOLME2 classes and functions that we will be demonstrating:
from aolme2 import vid, spr, load_img, plot_img, clean, TSP, img_fill

print ( "Robot distance simulation")
dist = 1000
print ("Assume that Robots sensor gives:")

while (dist>10):
    print ("Robots moves closer...")
    dist = dist - 10
    print ("Robot must sense the distance to target again.")
    print ("dist=", dist)
print ("Final: dist=", dist)
