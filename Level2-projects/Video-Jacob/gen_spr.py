import sys
import numpy as np
import pylab as pl
import cv2
from roipoly import roipoly 
import pickle 




# import image to convert into ROI
objectImage=cv2.imread(str(sys.argv[1]))
img = cv2.cvtColor( objectImage, cv2.COLOR_RGB2GRAY )

# show the image
pl.imshow(img, interpolation='nearest', cmap="Greys")
pl.colorbar()
pl.title("left click: line segment         right click: close region")

# let user draw first ROI
ROI1 = roipoly(roicolor='r') 

# convert ROI into mask
maskBool=ROI1.getMask(img) 
b  = maskBool.astype(int)*255
roiMask=b.astype(np.uint8)

# extract rectangular boundary region of the irregular region
r=[int(round(min(ROI1.allypoints))),int(round(min(ROI1.allxpoints))),int(round(max(ROI1.allypoints))),int(round(max(ROI1.allxpoints)))]


# Extract the sprite name without the extension of the image
SpriteName = str(sys.argv[1].rsplit(".")[0])

# Generate a single list with all the information needed in AOLME2 library
SpriteInfo = [SpriteName,objectImage,roiMask,r ]



# Store in a pickle file to be retrieved by AOLME2 library
with open('{}.pickle'.format(SpriteName), 'wb') as f:
            pickle.dump(SpriteInfo, f, pickle.HIGHEST_PROTOCOL)

print("Wrote {} sprite in pickle file".format(SpriteName))