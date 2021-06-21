import AOLMERobots as gopi
import cv2

# Setup the val,es to detect your range.
red_range   = [160,255]  #Red_min and Red_max
green_range = [0,40]      # Enter Green_min and Green_max
blue_range  = [0,57]   # Enter Blue_min and Blue_max
max_area = 8000
min_area = 4000 # Enter minimum area
area = 0
while (area < min_area):
    img = gopi.get_image()
    x,y,area = gopi.get_img_object_center(img, red_range, green_range, blue_range)

    x0 = img.shape[0]/2  # Column center of the image.
    obj_dist = x - x0    # Deviation from the center

    # Decide how to move the robot:
    print(obj_dist);
    if obj_dist >= 0: #image object
        if (obj_dist >50):
            print("Robot is too far to the left")
            print("Robot needs to turn right")
            gopi.rt(0.3)
        else:
            print("Robot needs to go forward")
            gopi.fw(0.3)

    else:
        if (obj_dist >(-50)): #object image
            print("Robot is too far to the right")
            print("Robot needs to turn forward")
            gopi.fw(0.3)
        else:
            print("Robot needs to turn left")
            gopi.lt(0.3)
    #if(area > max_area):

    #Display the image from the Robot
    cv2.imshow("Robot view", img)
    cv2.waitKey(10)
    print('Area = ', area)
gopi.lt(2)
gopi.fw(0.2)
gopi.bw(0.2)
gopi.fw(0.2)
gopi.bw(0.2)
print('Find object')
cv2.destroyAllWindows()
