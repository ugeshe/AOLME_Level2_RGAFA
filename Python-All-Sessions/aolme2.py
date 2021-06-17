# -*- coding: utf-8 -*-
"""
aolme2 library

help_all() provides help for all of the functions and classes.
"""

import numpy as np
import cv2
import math
import pickle
import matplotlib.pyplot as plt
import sys
from pathlib import Path
import itertools


def help_all():
    """
    Provides a list of all of the functions
    and classes in the module.
    """
    
    list_funs = """            
        Functions for manipulating images:            
        plot_img():    plots an image.
        load_img():    loads an image from disk.
        make_img():    initialize an image.
        img_im_fill(): image fill command. 
        img_hex2cv():  convert hex image to new image format.
        img_resize():  resizes the original image.
        To see an example, type: 
            help(make_img)
        
        TSP functions:
        show_tours():  prints out all possible tours.
        
        TSP class:
        To see all of the class functions, type:
            help(TSP)
                        
        Sprite Class:        
        To see an example, type:
            help(spr.fill)
        To see all of the class functions, type:
            help(spr)
        
        Video Class:
        To see a video example, type:
            help(vid.init_video)
        To see the functions that are available, type:
            help(vid)            
            
        Clean up functions:
        clean():       removes all figures.
        reset          eliminates all the variables.

        Others:                
        colorConv():   converts strings to (Red, Green, Blue).        
        
        help(<className>.<MethodName>)   to learn more about a method.
        print(str(<classInstanceName>))  for a printable version.
        print(repr(<classInstanceName>)) for internal debugging info.
        """
    print(list_funs)

# TSP related functions
def show_tours(num_of_cities):
    """ displays all possible tours for a
    given number of cities to visit.
    Example:
        num_of_cities = 3
        show_tours(num_of_cities)
    """
    Max_city_limit = 10
    if (num_of_cities > Max_city_limit):
        print("ERROR in show_perms():")
        print(("num_of_cities={}>{} is too large for me :-)").format(
                num_of_cities, Max_city_limit))
        return
    
    # Generate all permutations
    print(" ")
    basic_list = list(range(2, num_of_cities+1, 1))
    all_perms  = list(itertools.permutations(basic_list))
    
    print("List of all permutations of 2 to ",
          num_of_cities, ":")
    print(all_perms)
            
    print("List of tours that brings us back to origin:")
    i = 1
    for tour in all_perms:
        t = list(tour)
        t = [1] + t
        t.append(1)
        print(i, t)
        i+=1
    
    
    
class TSP:   
    def __init__(self, list_of_coords):
        """ Initializes the TSP problem with a list of
        coordinate points. The coordinate points represent
        the locations of each city.
            Example:
               # City coordinates:
               #  City 1: [0, 0]
               #  City 2: [1, 2]
               #  City 3: [5, 3]
               list_of_coords = [[0, 0], [10, 20], [50, 30], [40, 60]]
               my_TSP = TSP(list_of_coords)
        """
        
        self.city_coords   = list_of_coords
        self.num_of_cities = len(list_of_coords)
       
    # Describe the class for debugging. Help can be provided using:
    #    print(repr(<instanceName>))
    def __repr__(self):
        """ Provides information for developers. """
        
        info = """ 
          The TSP class provides tour functions for the TSP
          problem. It computes tour lengths and prints tours.
          """          
        return(info)
        
    def __str__(self):
        """ Provides information for users of the class.
        The information is available using:
            print(name_of_the_object)
        """
        
        info = ("TSP: Number of cities={}\n".format(self.num_of_cities))
        info += ("List of coordinate points:\n")
        info += str(self.city_coords)
        return(info)
    
    # TODO: ???? Create valid_tour function
    
    def tour_length(self, tour):
        """
        Computes the length of a tour.
        The parameter tour lists the city order.
        Example:
            city_coords = [[0, 0], [1, 2], [5, 3]]
            my_TSP    = TSP(city_coords)
            tour1     = [1, 3, 2, 1]
            tour1_len = my_TSP.tour_length(tour1)
            print("tour=", tour1, "has length ", tour1_len)
        """
        
        if (len(tour)-1 != self.num_of_cities):
            print("ERROR in tour_length()")
            print("Number of cities = ", self.num_of_cities)
            print("Tour = ", tour)
            print("does not have enough cities!")
            return
        
        city1 = tour[0]
        if (city1 != 1):
            print("ERROR in tour_length()")
            print("Start city must be 1")
            print("Tour = ", tour)
            print("does not start at 1")
            return
        
        cityN = tour[-1]
        if (cityN != 1):
            print("ERROR in tour_length()")
            print("Final city must be 1")
            print("Tour = ", tour)
            print("does not end at 1")
            return
        
        dist = 0.0    
        for i in range(0, len(tour)-1, 1):
            j1 = tour[i]-1
            j2 = tour[i+1]-1            
            c1 = self.city_coords[j1]
            c2 = self.city_coords[j2]
            hyp = math.sqrt((c1[0]-c2[0])**2 
                            + (c1[1]-c2[1])**2)
            dist += hyp
        
        return(dist)
        
    def plot_tour(self, tour, num_of_rows, num_of_cols):
        """
        Plots a given tour.
        Example:
            list_of_coords = [[0, 0], [10, 20], [50, 30]]
            my_TSP    = TSP(city_coords)
            tour1     = [1, 3, 2, 1]
            tour1_len = my_TSP.tour_length(tour1)
            print("tour=", tour1, "has length ", tour1_len)
            my_TSP.plot_tour(tour1, 100, 100)
        """
        
        # Find the limits:
        c = np.array(self.city_coords)
        row_min = np.min(c[:,0])
        row_max = np.max(c[:,0])
        col_min = np.min(c[:,1])
        col_max = np.max(c[:,1])
                
        # Adjust the text for cities to be reasonable:
        offset = np.min([0.1*(col_max-col_min), 1])
        
        # Plot all of the points.
        plt.figure()
        plt.axis('image')
        for i in range(0, len(tour)-1, 1):            
            j1 = tour[i]-1
            j2 = tour[i+1]-1
            c1 = tuple(self.city_coords[j1])
            c2 = tuple(self.city_coords[j2])
            c1 = (c1[1], c1[0])
            c2 = (c2[1], c2[0])                        
            plt.plot((c1[0], c2[0]), (c1[1], c2[1]), 'b-')
            circle1=plt.Circle(c1, radius=1, color='r', fill=False)
            circle2=plt.Circle(c2, radius=1, color='r', fill=False)                      
            plt.gcf().gca().add_artist(circle1)
            plt.gcf().gca().add_artist(circle2)
            plt.text(c1[0]+offset, c1[1]+offset, str(j1+1), fontsize=14)
            plt.text(c2[0]+offset, c2[1]+offset, str(j2+1), fontsize=14)
            
        # Reverse the limits:
        plt.ylim(1.2*float(row_max), 0.8*float(row_min))
        plt.xlim(0.8*float(col_min), 1.2*float(col_max))
        plt.show()        
                
        
        
    def best_tour(self):
        """ Computes the best tour.
        Example:
            city_coords = [[0, 0], [10, 20], [50, 30], [40, 60]]            
            my_TSP = TSP(city_coords)
            my_TSP.best_tour()
        """
        
        # Generate all permutations
        basic_list = list(range(2, self.num_of_cities+1, 1))
        all_perms  = list(itertools.permutations(basic_list))
        
        # Generate valid tours:
        i = 1
        min_dist = math.inf
        for tour in all_perms:
            t = list(tour)
            t = [1] + t
            t.append(1)
                        
            dist = self.tour_length(t)
            
            print("Tour = ", t)
            print("Distance = ", dist)
            
            if (dist < min_dist):
                best_tour = t
                min_dist  = dist
        
        # Fix rows and cols later
        self.plot_tour(best_tour, 100, 100)
        print("Best tour is")
        print(best_tour)
        print("It has distance = ", min_dist)
    
          






def clean():
    """ 
     Closes all Figures and all OpenCV windows.
     If you also want to eliminate all of the 
     variables, issue:
         reset
     at the IPython prompt.
     Example:
         clean()
    """
    
    plt.close("all")
    cv2.destroyAllWindows()
    

def load_img(fileName):
    """ loads the image specified in fileName.
       If the image does not exist, it prints an error message.
    Example:
        img = load_img("backgroundMario.jpg")
        plot_img(img, "Image Ex")
    """
    
    if Path(fileName).is_file():
        print("Reading file = ", fileName)
    else:
        print("In load_img(),")
        print("Unable to open file = ", fileName)
        print("Make sure the file is in the current directory!")
        sys.exit(0)
    
    img = cv2.imread(fileName)
    return(img)
    
    
def plot_img(img, title):
    """ 
    This is the standard function for plotting
    images manipulated in OpenCV. The image is
    assumed to be in BGR format and it is converted
    to RGB for display.
        
    Example:                    
        import aolme2
        bac=load_img("backgroundMario.jpg")
        plot_img(bac, "Image Ex")
    """
        
    plt.figure()
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()
    plt.pause(0.01)    


def colorConv(color):
    """ 
     Converts hex color strings to (Red, Green, Blue).
     Example:
         print(colorConv("FFAA12"))
    """
    
    if (isinstance(color, str)):
        Red   = int(color[0:2], 16) # Base 16 conversion
        Green = int(color[2:4], 16)
        Blue  = int(color[4:6], 16)
    else:
        print("colorConv(color={})".format(color))
        print("ERROR: {} is not a string!".format(color))
    
    return((Red,Green,Blue))
        

def make_img(num_of_rows, num_of_cols, color):
    """ 
    creates a NumPy array to store a colored frame.
    The array colors are stored in BGR to be 
    compatible with OpenCV. However, they are 
    displayed using RGB.
    Example:
      blue_img = make_img(10,12,"0000FF")
      plot_img(blue_img, "blue")
      red_img  = make_frame(11,12,(255,0,0))
      plot_img(red_img, "red")
    """
    
    # A color image with three components
    img = np.zeros((num_of_rows, num_of_cols, 3), dtype=np.uint8)
    if (isinstance(color, str)):
        Red, Green, Blue = colorConv(color)        
    else:
        Red, Green, Blue = color
    
    # BGR order:
    img[:,:,0] = Blue
    img[:,:,1] = Green
    img[:,:,2] = Red    
    return(img)

def img_resize(img, scale_factor):
    """
    Resizes the image up (scale_factor>1) or down (scale_factor<1).
    Example:
        bac=load_img("backgroundMario.jpg")
        print("Original size = ", bac.shape)        
        img = img_resize(bac, 2)
        print("New size = ", img.shape)
    """
    
    res = cv2.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
    return(res)
    


def img_fill(img, rows, cols, color):
    """
    places color on an image as given by rows, cols
    Example:
        # Colors
        black = "000000"
        red   = "FF0000"
        
        img = make_img(10, 10, black)
        
        start_row = 0
        end_row   = 1
        rows = [start_row, end_row]
        
        start_col = 2
        end_col   = 3
        cols = [start_col, end_col]
        
        img_fill(img, rows, cols, red)
        plot_img(img, "red on black")
        
        img = load_img("clock.jpg")
        img_fill(img, [0, 100], [0, 100], red)
        plot_img(img, "img fill ex")
        
        my_video = vid("Video 1", 1000, 1000)
        my_video.set_back
    """
    
    try:
        if (isinstance(color, str)):
            Red, Green, Blue = colorConv(color)
        else:
            Red, Green, Blue = color
            
        # Loc:
        r1, r2 = rows
        c1, c2 = cols
        
        # Check:
        if (r1>r2):
            print("img_im_fill(): rows={}".format(rows))
            print("ERROR: start_row={}>end_row={}".format(r1,r2))
            print("SUGGESTION: Reverse the row order?")
            return
        
        if (c1>c2):
            print("img_im_fill(): cols={}".format(cols))
            print("ERROR: start_col={}>end_col={}".format(r1,r2))
            print("SUGGESTION: Reverse the column order?")
            return
        
        # BGR order:
        img[r1:r2+1, c1:c2+1,0] = Blue
        img[r1:r2+1, c1:c2+1,1] = Green
        img[r1:r2+1, c1:c2+1,2] = Red
    
    except:
        print("ERROR in img_im_fill()!")
        print("Called using:")
        print("img_im_fill(img, rows, cols, color)")
        print("rows={}, cols={}, color={}".format(rows,cols, color))
    
    
def img_hex2cv(frame_hex):
    """ 
    converts hex frame to CV format.
    Example:
        cols=2
        rows=3
        frame_0 = [["00"]*cols for row in range(rows)]
        img = img_hex2cv(frame_0)
        plot_img(img, "Black image")
    """
    
    # Create the image array:
    num_of_rows = len(frame_hex)
    num_of_cols = len(frame_hex[0])
    img = make_frame(num_of_rows, num_of_cols, (0,0,0))
    
    for i in range(num_of_rows):
        for j in range(num_of_cols):
            color = frame_hex[i][j]
            if (len(color)==2):
                # Grayscale:
                int_color = int(color, 16)
                Red   = int_color
                Green = int_color
                Blue  = int_color
            else:
                Red   = int(color[0:2], 16) 
                Green = int(color[2:4], 16)
                Blue  = int(color[4:6], 16)
            
            # BGR order
            img[i,j,0] = Blue
            img[i,j,1] = Green
            img[i,j,2] = Red
            
    return(img)
                        

# Sprite image class
class spr:
    # Initialize the class
    def __init__(self, num_of_rows=0, num_of_cols=0):
        """ spr(num_of_rows, num_of_cols)
         Creates a sprite image.
         Example:
             num_of_rows = 10
             num_of_cols = 10
             my_sprite = spr(num_of_rows, num_of_cols)
             print(my_sprite)
        """
        
        self.num_of_rows = num_of_rows
        self.num_of_cols = num_of_cols
        
        # Create an empty roi: 
        self.sprite_roi = np.zeros((num_of_rows, num_of_cols), dtype=np.uint8)
        
        # Create an empty image:
        white = "FFFFFF"
        self.sprite_img = make_img(num_of_rows, num_of_cols, white)
    
    def set_sprite(self, sprite_name):
        """
        Reads a file called sprite_name from the local directory and 
        saves it with the same name.
        Example:            
            # Generate the Sprite by running
            # the following at the Anaconda command prompt:
            python gen_spr.py BowserFull.png
            # The above line is run OUTSIDE Spyder
            
            # Set the sprite here:
            my_sprite = spr()
            my_sprite.set_sprite("BowserFull")
            my_sprite.show("Bowser")
        """
            
        print("set_sprite(sprite_name={})".format(sprite_name))
        
        fileName = '{}.pickle'.format(sprite_name)
        if Path(fileName).is_file():
            print("Reading file = ", fileName)
        else:
            print("Unable to open file = ", fileName)
            print("Please check the name again!")
            print("Make sure that the file is in the current directory")
            sys.exit(0)
            
        with open(fileName, 'rb') as f:
            SpriteInfo=pickle.load(f)
            
        # Variables sprite_name and sprite_img from Pickle file
        sprite_name = SpriteInfo[0]
        read_sprite_img = SpriteInfo[1]
            
        # Variable obj_roi is the mask (0 or 255) generated with roipoly library
        read_sprite_roi = SpriteInfo[2]
        
        # Corners values of the Rectangular ROI around the sprite
        read_sprite_rec = SpriteInfo[3]                
        
        # Re-center
        min_row, min_col, max_row, max_col = read_sprite_rec
        
        print(read_sprite_roi.shape)
        
        self.num_of_rows = max_row-min_row
        self.num_of_cols = max_col-min_col
        self.sprite_rec = [0, 0, self.num_of_rows, self.num_of_cols]        
        self.sprite_img = read_sprite_img[int(min_row):int(max_row+1), int(min_col):int(max_col+1),:]
        self.sprite_roi = read_sprite_roi[int(min_row):int(max_row+1), int(min_col):int(max_col+1)]
                
        
    def fill(self, rows, cols, color):
        """
        Modifies a rectangle of the sprite image.
        
        Example:
            # Colors            
            red   = "FF0000"
            
            spr_ex = spr(10, 10) # Initialize
        
            start_row = 0
            end_row   = 1
            rows = [start_row, end_row]
        
            start_col = 2
            end_col   = 3
            cols = [start_col, end_col]
        
            spr.fill(rows, cols, red)
            spr.show("Red")
        """
        
        # Put it in the image
        img_im_fill(self.sprite_img, rows, cols, color)
        
        # Update the ROI
        r1, r2 = rows
        c1, c2 = cols
        self.sprite_roi[r1:(r2+1), c1:(c2+1)] = 255
        
                
    def show(self, plot_name):
        """ displays the sprite image.
            To see an example, type:
                help(spr.fill)
        """
        objfull= self.sprite_img
        objroi= self.sprite_roi
        
        sprite_size_rows=objfull.shape[0]
        sprite_size_cols=objfull.shape[1]
        
        
        maskObj=np.zeros((sprite_size_rows,sprite_size_cols,3),  dtype=np.uint8)
        maskObj[:,:,0]=objroi
        maskObj[:,:,1]=objroi
        maskObj[:,:,2]=objroi
        
        sprite_no_background = np.ones((sprite_size_rows,sprite_size_cols,3),  dtype=np.uint8)
        sprite_no_background=sprite_no_background*255
        np.copyto(sprite_no_background, objfull, where=(maskObj>0))
        
        plot_img(sprite_no_background, plot_name)
        
    def get_sprite(self): ## Added self.sprite_rec
        obj = [self.sprite_img, self.sprite_roi, self.sprite_rec, self.num_of_rows, self.num_of_cols]
        return(obj)
        
    
    # Provide debug information
    def __repr__(self):
        """ spr is used for creating sprites."""
        
        info = """
          The spr class implements sprites as images with a
          region of interest. It does not include any sprite
          manipulation functions. These are implmented in vid.
          
          It uses sprite_img to store the image and sprite_roi
          to store the region of interest.
          
          It communicates with the vid class using the 
              get_sprite() method.
          """
        return(info)        
    
    # Provide output
    def __str__(self):
        """ Returns the size of the sprite. """
        
        str_val = "Sprite({}, {})".format(self.num_of_rows, self.num_of_cols)
        return(str_val)
    
    

# vid class implements the video class.
# To create an instance, refer to __init__ function.
# A summary of the class methods and examples can be provided using:
#   help(vid)
# We can access a developer's view of the class using:
#   print(repr(<instance_name>))
# We can access a fast printout of the class using:
#   print(str(<instance_name>))
# or simply using:
#   print(<instance_name>)        
class vid:
    # Define variables to be shared by all instances.

    # Initialize the dictionary of background and sprites images.        
    # These variables are to be shared by all instances.
    # They can be shared across videos.
    dictionary_Backgrounds = {}
    dictionary_Sprites  = {}    
    
    def __init__(self, video_name, num_of_rows, num_of_cols):
        """ vid(video_name, num_of_rows, num_of_cols)
              Initializes a video with video_name where
              each video frame is of size num_of_rows by num_of_cols.
            Example:
                my_video=vid('MyVideoName', 20, 20)
        """
        
        print("aolme2(video_name={}, num_of_rows={}, num_of_cols={})".format(
                video_name, num_of_rows, num_of_cols))
        
        self.video_name = video_name
        self.video      = []
        self.num_of_rows = num_of_rows
        self.num_of_cols = num_of_cols
        self.move_path = []
        
        
    # Describe the class for debugging. Help can be provided using:
    #    print(repr(<instanceName>))
    def __repr__(self):
        """ Provides information for developers. """
        
        info = """ 
          The vid class implements level 2 
          functions for making videos with real images.
          Videos are constructed using backgrounds and 
          sprites.
          
          The backgrounds and sprites are stored in:
              dictionary_Backgrounds
              dictionary_Sprites
          The actual video is stored in:
              video[frame_number]
              num_of_rows, num_of_cols, and other video variables.
          """          
        return(info)
    
    # Provide a string representation for the class.
    # Use print(<instanceName>) or print(str(<instanceName>))
    # to see the information.
    def __str__(self):
        """ Prints the name of the video and its size. """
        
        str_val = "Video name={} (rows={}, cols={})\n".format(
                self.video_name, 
                self.num_of_rows, 
                self.num_of_cols) 
        str_val += "Sprites = {}\n".format(
                list(self.dictionary_Sprites.keys()))
        str_val += "Background images = {}\n".format(
                list(self.dictionary_Backgrounds.keys()))
        str_val += "Number of frames = {}\n".format(
                len(self.video))    
        for name in list(self.dictionary_Sprites.keys()):
            str_val += "{} has travelled {:.2f} pixels.\n".format(
                    name, self.get_distance(name))
            
        return(str_val)    
         
        
    def set_back(self, back_name, back_img):
        """
        Sets the background image name back_name
        using back_img which represents an image.
        Example in init_video():
            help(vid.init_video)         
        """
        
        # Check the size of the image and make sure that it is big enough.
        num_of_rows, num_of_cols, colors = back_img.shape
        if (num_of_rows<self.num_of_rows) or (num_of_cols<self.num_of_cols):
            print("ERROR: Background image is too small in set_back().\n")
            print("Background image name = ", back_name, "\n",
                  "number of rows = ", num_of_rows, "\n",
                  "number of cols = ", num_of_cols)
            print("Image needs to be at-least as large as:\n",
                  "number of rows = ", self.num_of_rows, "\n",
                  "number of cols = ", self.num_of_cols)
            print("You can resize an image using img_resize().")            
            return
        
        
        
        try:
            self.dictionary_Backgrounds[back_name] = back_img
        except:
            print("set_back(back_name={}, back_img)".format(back_name))
            print("ERROR: Please check background name = ", back_name)
            print("I do not have this background in the class!")
            sys.exit(0)
       
        
    def set_sprite(self, sprite_name, spr_var):
        """
        Creates a sprite with name sprite_name from
        a sprite_var created using the spr class.        
        """
        
        try:
            spr_img, spr_roi, spr_rec, num_of_rows, num_of_cols = spr_var.get_sprite()  
        except:
            print("ERROR in set_sprite()")
            print("Make sure that the sprite variable name is correct")
            sys.exit(0)
        
        newRow   = 0
        newCol   = 0
        
        distance_moved = 0
        First_time = True
        
        path_coordinates = []
        
        ## Changed spr_rec
        obj = [spr_img, spr_roi, spr_rec,newRow,newCol,distance_moved,First_time,path_coordinates]
        self.dictionary_Sprites[sprite_name] = obj


    def init_video(self, back_name, start_row, start_col):
        """ Add the first background to the video 
            Arguments start_row & start_col are used for backgrounds larger 
            than the video frame size.
            
            Example:
              bac=load_img("backgroundMario.jpg")
              num_rows=500
              num_cols=500

              # Create new video 
              myvideo = vid('First video',num_rows,num_cols)

              # Add background to the video
              myvideo.set_back('back1', bac)
              myvideo.init_video('back1', 0, 0)
              myvideo.show_last_frame()
        """
        
        r=[start_col,start_row,self.num_of_cols,self.num_of_rows]
        
        try:
            im=self.dictionary_Backgrounds[back_name]
        except:
            print("ERROR in init_video()")
            print("I cannot find background name = ", back_name)
            print("Make sure to use the set_back() method to initialize it first")
            sys.exit(0)
        
        
        if (start_row + self.num_of_rows) > (im.shape[0]): 
            print("ERROR in init_video()")
            print("start_row exceeds limit = ", im.shape[0])
            sys.exit(0) 
        
        if (start_col + self.num_of_cols) > (im.shape[1]): 
            print("ERROR in init_video()")
            print("start_col exceeds limit = ", im.shape[1])
            sys.exit(0) 
            
       
            
        imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]                
        self.video.append(imCrop)
        
    def get_size(self):  
        """ Returns the numbers of rows and columns defined for the video"""    
        print('rows: {} and cols: {}'.format(self.num_of_rows,self.num_of_cols))
        return (self.num_of_rows, self.num_of_cols)
    
    def set_new_frame(self, back_name,start_row, start_col):
        """ Add the background object 'back_name' as a new frame to the video
            Arguments start_row and start_col behave as in the init_video method """       
        r=[start_col,start_row,self.num_of_cols,self.num_of_rows]
                
        try:
            im=self.dictionary_Backgrounds[back_name]
        except:
            print("ERROR in set_new_frame()")
            print("I cannot find background name = ", back_name)
            print("Make sure to use the set_back() method to initialize it first")
            sys.exit(0)
        
        if (start_row + self.num_of_rows) > (im.shape[0]): 
            print("ERROR in set_new_frame()")
            print("start_row exceeds limit = ", im.shape[0])
            sys.exit(0) 
        
        if (start_col + self.num_of_cols) > (im.shape[1]): 
            print("ERROR in set_new_frame()")
            print("start_col exceeds limit = ", im.shape[1])
            sys.exit(0) 

        imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
        self.video.append(imCrop)
    
    def place_obj(self, objfull, objroi,objaxis, place_row, place_col):
        """ Internal function that place the sprite (object) in place_row and place_col
            using the arguments objroi and objaxis to generate a mask to be applied over the lastest background.
            Returns an overwritten last frame of video with the sprite in the desired place"""
        
        # 1. Retrieve the last video frame else print a warning.
        if not self.video[:] :
            print("ERROR in place_obj()")
            print("Make sure to initialize the video first")
            sys.exit(0)
        else:
            vidframe=self.video[-1]
        
        if (place_row > self.num_of_rows ):
            print("ERROR in place coordinates()")
            print("Sprite row_center outside video limit = ", place_row)
            print("Must be less than = ", self.num_of_rows)
            sys.exit(0) 
            
        if (place_col > self.num_of_cols ):
            print("ERROR in place coordinates()")
            print("Sprite col_center outside video limit = ", place_col)
            print("Must be less than = ", self.num_of_cols)
            sys.exit(0) 
            
            
        # 2. Initialize the image containing the sprite (objfull) and MASK (objroi)           
        
        objFull_new_cols=objfull.shape[1]
        objFull_new_rows=objfull.shape[0]
                      
        objfull=objfull[:objFull_new_rows,:objFull_new_cols,:]
        objroi=objroi[:objFull_new_rows,:objFull_new_cols]
        
        ###################################################### 
        
        rowREClength=objaxis[2]-objaxis[0]
        colREClength=objaxis[3]-objaxis[1]
        
        rowRECcenter=int(round(rowREClength/2) + objaxis[0])
        colRECcenter=int(round(colREClength/2) + objaxis[1])
        
        #########################
#        (h, w) = objfull.shape[:2]
#        (cX, cY) = (w // 2, h // 2)
#        rowRECcenter=cY
#        colRECcenter=cX

        
        ###### Trim Rectangular Region Of Interest (REC) to fit the background
        
        ### center to top:
        ctop=round(rowREClength/2)
         ### center to bottom:
        cbottom=rowREClength-ctop
        ### center to right:
        cleft=round(colREClength/2) #### 122
        ### center to left:
        cright=colREClength-cleft
        
                
        if ctop > place_row:
            ctop = place_row 
        if cbottom > (self.num_of_rows-place_row):
            cbottom = (self.num_of_rows-place_row)
        if cleft > place_col:
            cleft = place_col
        if cright > (self.num_of_cols-place_col):
            cright = (self.num_of_cols-place_col)
        
        objaxis2=[0,0,0,0]
        objaxis2[0]=int(rowRECcenter-ctop)
        objaxis2[1]=int(colRECcenter-cleft)
        objaxis2[2]=int(rowRECcenter+cbottom)
        objaxis2[3]=int(colRECcenter+cright)
       
        ######################################################
        
        maskObj=np.zeros((objFull_new_rows,objFull_new_cols,3),  dtype=np.uint8)
        maskObj[:,:,0]=objroi
        maskObj[:,:,1]=objroi
        maskObj[:,:,2]=objroi
        
        
        # 3. Calculate masked object (objSel)
        
        objSel = np.zeros((objFull_new_rows,objFull_new_cols,3),  dtype=np.uint8)
        np.copyto(objSel, objfull, where=(maskObj>0))
        
        # 4. Moved masked object to desired location (place_row,place_col) 
            
            #A rectangular region (REC) is defined to the boundaries of the irregular region of interest:       
            # objaxis=[minRow,minCol,maxRow,maxCol]
        rowREClength=objaxis2[2]-objaxis2[0]
        colREClength=objaxis2[3]-objaxis2[1]
        
        rowREChalf=round(rowREClength/2)
        colREChalf=round(colREClength/2)
        
            #Empty array (same size as video) to hold the REC
        objFrame= np.zeros((self.num_of_rows,self.num_of_cols,3),  dtype=np.uint8)
            
            #The center of REC is placed at desired location (plc_row,plc_col)      
        flowerRow=place_row-ctop
        fupperRow=place_row+cbottom
        flowerCol=place_col-cleft
        fupperCol=place_col+cright
        
        objFrame[flowerRow:fupperRow,flowerCol:fupperCol,:] = objSel[objaxis2[0]:objaxis2[2],objaxis2[1]:objaxis2[3],:]
        
        # 5. Prepare inverted mask (same size as video)       
        maskFrame= np.zeros((self.num_of_rows,self.num_of_cols,3),  dtype=np.uint8)
        
        maskFrame[flowerRow:fupperRow,flowerCol:fupperCol,:] = maskObj[objaxis2[0]:objaxis2[2],objaxis2[1]:objaxis2[3],:]
        
        maskFrame = cv2.bitwise_not(maskFrame)
        
        # 6. Calculate inverted masked background        
        frame2update = np.zeros(vidframe.shape,  dtype=np.uint8)
        np.copyto(frame2update, vidframe, where=(maskFrame>0))
        
        
        # 7. Calculate new frame with object and background           
        frameFinal=objFrame+frame2update        

        # 8. Save the object location into a dictionary for the current video.           
        newCoord=[place_row,place_col]

        # 9. Update the last video frame.         
        self.video[-1]=frameFinal
        
        # 10. Return the new coordinates
        return newCoord
    
    def place_sprite(self, sprite_name, start_row, start_col):
        """ Returns the last video frame with the sprite placed in the start_row & start_col position 
            The center of the ROI in the sprite is used to place coordinates start_row & start_col 
            The sprite is cropped if it is not able to fit in the frame """

        # 1. Extract information from object dictionary (dictionary_Sprites)
        try:
            objfull=self.dictionary_Sprites[sprite_name][0]
            objroi=self.dictionary_Sprites[sprite_name][1]
            roiaxis=self.dictionary_Sprites[sprite_name][2]
        except:
            print("ERROR in place_sprite()")
            print("Check sprite name = ", sprite_name)
            print("I cannot find it!")
            sys.exit(0)
            
        
        place_row=start_row
        place_col=start_col
        
        # 2. Call place object function (.place_obj())
        newCoord = self.place_obj(objfull, objroi, roiaxis, place_row, place_col)
        
        
        
        
        distance_moved=self.dictionary_Sprites[sprite_name][5]
        
        # Calculate Pythegorean distance
        Previous_row=self.dictionary_Sprites[sprite_name][3]
        Previous_col=self.dictionary_Sprites[sprite_name][4]
        Pythagorean_distance = np.sqrt((Previous_row - place_row)**2 + (Previous_col - place_col)**2)
        
        # Check if is the first time the sprite is being placed
        if (self.dictionary_Sprites[sprite_name][6] == True) :
            distance_moved = 0
        else: 
            distance_moved = distance_moved + Pythagorean_distance
        
        # Update Flag and distance to sprite
        self.dictionary_Sprites[sprite_name][6] = False
        self.dictionary_Sprites[sprite_name][5] = distance_moved
        
        # 3. Update coordinates 
        self.dictionary_Sprites[sprite_name][3]=newCoord[0]
        self.dictionary_Sprites[sprite_name][4]=newCoord[1]
        
        # Init path coordinates
        new_coord_entry = (place_col,place_row)
        self.dictionary_Sprites[sprite_name][7].append(new_coord_entry) 
        
    def get_sprite_loc(self, sprite_name):
        """ Returns the row and column coordinates of the sprite.
        Example:
            ... after you create the video and place the sprite
            ... spr_name must be a valid sprite name.
            row_center, col_center = my_video.get_sprite_loc(spr_name)
        """
        try:
            Row=self.dictionary_Sprites[sprite_name][3]
            Col=self.dictionary_Sprites[sprite_name][4]
        except:
            print("ERROR in get_sprite_loc()")
            print(sprite_name, " has not been found")
            print("Make sure that the name is correct!")
            sys.exit(0)
        
        return (Row, Col)

        
    def move_sprite(self, sprite_name, row_motion, col_motion, Trace = False):
        """ Returns the last video frame with the sprite moved from previous position
            Arguments 'row_motion' & 'col_motion' are the amount of pixels to be moved 
        """
        
        
        # Retrieve the last saved location of the object from previous frame.
        try:
            oldRow=self.dictionary_Sprites[sprite_name][3]
            oldCol=self.dictionary_Sprites[sprite_name][4]
        except:
            print("ERROR in move_sprite()")
            print(sprite_name, " has not been found")
            print("Make sure that the name is correct!")
            sys.exit(0)
            
        
        # Call place_sprite() with new coordinates.
        newCoord_row = oldRow + row_motion        
        newCoord_col =  oldCol + col_motion 

        
        # 1. Check the amount of movement to be inside the video
        if ((newCoord_row < 0) or (newCoord_row > self.num_of_rows)):
            print(" Rows Coordinates {} out of range".format(row_motion))
            sys.exit(0)
            
        if ((newCoord_col < 0) or (newCoord_col > self.num_of_cols)):
            print(" Columns Coordinates {} out of range".format(col_motion))
            sys.exit(0)
        
        
        self.place_sprite(sprite_name, newCoord_row,newCoord_col)  
        
        # Keep track of the latest coordinate to later draw a path
        #if Trace :            
        #    new_coord_entry = (newCoord_col,newCoord_row)
        #    self.dictionary_Sprites[sprite_name][7].append(new_coord_entry) 
        
        # 3. Update coordinates 
        self.dictionary_Sprites[sprite_name][3]=newCoord_row
        self.dictionary_Sprites[sprite_name][4]=newCoord_col 
 
           
    def rotate_sprite(self, sprite_name, row_center, col_center, rot_angle):
        """ Returns the last video frame with the sprite rotated 'rot_angle' degrees
            Arguments row_center & col_center place the sprite within the frame (similar to place_sprite) 
        """
        # 1. Extract information from object dictionary (dictionary_Sprites)
        try:
            objfull=self.dictionary_Sprites[sprite_name][0]
            objroi=self.dictionary_Sprites[sprite_name][1]
            roiaxis=self.dictionary_Sprites[sprite_name][2]
        except:
            print("ERROR in rotate_sprite()")
            print("I cannot find sprite = ", sprite_name)
            print("Check the name!")
            sys.exit(0)
        
        # 2. Define extra variables for "objfull" and "objroi" rotation
        h=roiaxis[2]-roiaxis[0]
        w=roiaxis[3]-roiaxis[1]
        
        
        cX =round(w/2) + roiaxis[1]
        cY =round(h/2) + roiaxis[0]
                
        M = cv2.getRotationMatrix2D((cX, cY), rot_angle, 1.0)
        cos = np.abs(M[0, 0])
        sin = np.abs(M[0, 1])
        
        # 3. Calculate new dimensions and translate center 
        nW = int((h * sin) + (w * cos))
        nH = int((h * cos) + (w * sin))
        
        M[0, 2] += (nW / 2) - cX
        M[1, 2] += (nH / 2) - cY
        
        # 4. Rotate "objfull" and "objroi"        
        objFullRotated = cv2.warpAffine(objfull, M, (nW, nH))
        objRoiRotated = cv2.warpAffine(objroi, M, (nW, nH))
        
        # 5. Calculate new lengths of rectangle to fit rotated REC       
        rowREClength=roiaxis[2]-roiaxis[0]
        colREClength=roiaxis[3]-roiaxis[1]
        
        
        nWREC = int((rowREClength * sin) + (colREClength * cos))
        nHREC = int((rowREClength * cos) + (colREClength * sin))
        
        # 6. Find center of the Rectangle region of interest (roiaxis)        
        rowRECcenter=round(rowREClength/2) + roiaxis[0]
        colRECcenter=round(colREClength/2) + roiaxis[1]
        
#        M = np.round_(M,3)
        
        # 7. Transform original center coordinates to new rotated cordinates  
#        newColCenter=int(round(round(M[0, 0]*colRECcenter,3) + round(M[0, 1]*rowRECcenter,3) + M[0, 2]))
#        newRowCenter=int(round(round(M[1, 0]*colRECcenter,3) + round(M[1, 1]*rowRECcenter,3) + M[1, 2]))
        
        newColCenter=M[0, 0]*colRECcenter + M[0, 1]*rowRECcenter + M[0, 2]
        newRowCenter=M[1, 0]*colRECcenter + M[1, 1]*rowRECcenter + M[1, 2]
        
        
        # 8. Calculate new boundaries of REC "roiaxis"
        RECaxisRotated=[int(round(newRowCenter-nHREC/2)),int(round(newColCenter-nWREC/2)),int(round(newRowCenter-nHREC/2+nHREC)),int(round(newColCenter-nWREC/2+nWREC))]
                

        # 9. Call function to place rotated object
        newCoord = self.place_obj(objFullRotated, objRoiRotated, RECaxisRotated, row_center, col_center)
        
        # 10. Update coordinates of the rotated object
        self.dictionary_Sprites[sprite_name][3]=newCoord[0]
        self.dictionary_Sprites[sprite_name][4]=newCoord[1]

    
        
    def scale_sprite(self, sprite_name, row_center, col_center, scale_factor):
        """ Returns the last video frame with the sprite scaled by 'scale_factor' 
            Arguments row_center & col_center place the sprite within the frame (similar to place_sprite) """
        
        # 1. Extract information from object dictionary (dictionary_Sprites)
        try:
            objfull=self.dictionary_Sprites[sprite_name][0]
            objroi=self.dictionary_Sprites[sprite_name][1]
            roiaxis=self.dictionary_Sprites[sprite_name][2]
        except:
            print("ERROR in scale_sprite()")
            print("I cannot find sprite = ", sprite_name)
            print("Check the name!")
            sys.exit(0)
        
        # 2. Calculate new dimensions of image (and mask) using scale_factor  
        dim = (int(round(objfull.shape[1] * scale_factor)), int(round(objfull.shape[0]*scale_factor)))
        
        # 3. Resized image (objFull) and mask (objroi)        
        objResized = cv2.resize(objfull, dim, interpolation = cv2.INTER_AREA)    
        maskResized = cv2.resize(objroi, dim, interpolation = cv2.INTER_AREA) 
        
        # 4. Calculate and center point of original Rectangular region of interest
        rowREClength=roiaxis[2]-roiaxis[0]
        colREClength=roiaxis[3]-roiaxis[1]
        
        rowRECcenter=rowREClength/2 + roiaxis[0]
        colRECcenter=colREClength/2 + roiaxis[1]
        
        # 5. Calculate new boundaries of REC
        newRowLen = int(round(rowREClength * scale_factor))
        newColLen = int(round(colREClength * scale_factor))
        
        newCenterRows= int(round(rowRECcenter* scale_factor))
        newCenterCols=int(round(colRECcenter* scale_factor ))
        
        
        newRowsHalf=int(round(newRowLen/2))
        newColsHalf=int(round(newColLen/2))
        
        # 6. Calculate the borders of the Rectangular Region of Interest
        r0=newCenterRows-newRowsHalf
        r1=newCenterCols-newColsHalf
        r2=newCenterRows+newRowLen-newRowsHalf
        r3=newCenterCols+newColLen-newColsHalf
        
        # 7. Set the boundaries of the REC to fit Image
        if r0 < 0:
            r0=0
        if r1 < 0:
            r1=0
        if r2 > maskResized.shape[0]:
            r2 = maskResized.shape[0]
        if r3 > maskResized.shape[1]:
            r3 = maskResized.shape[1]
        r=[r0,r1,r2,r3]
        
        # 8. Call place object function to fit scaled image
        newCoord = self.place_obj(objResized, maskResized, r, row_center, col_center)
        
        # 9. Update coordinates of the scaled object
        self.dictionary_Sprites[sprite_name][3]=newCoord[0]
        self.dictionary_Sprites[sprite_name][4]=newCoord[1]


    def flip_hor(self, sprite_name, place_row, place_col):
        """ Flip the sprite horizontally."""

        # 1. Extract information from object dictionary (dictionary_Sprites)
        objfull=self.dictionary_Sprites[sprite_name][0]
        objroi=self.dictionary_Sprites[sprite_name][1]
        objaxis=self.dictionary_Sprites[sprite_name][2]
        
        # 2. Flip sprite and mask
        objfullFlipHor=np.fliplr(objfull)
        objroiFlipHor=np.fliplr(objroi)
        
        # 3. Flip borders of REC
        objaxisFlipHor = [0,0,0,0]
        N_Cols=objfull.shape[1]
        N_Rows=objfull.shape[0]
        
        px0=objaxis[1]
        py0=objaxis[0]
        
        xInit = int(N_Cols/2)
        yInit = 0
        xFinal = xInit
        yFinal = N_Rows
        
        
        dx  = xFinal - xInit
        dy  = yFinal - yInit
        
        a   = (dx * dx - dy * dy) / (dx * dx + dy*dy)
        b   = 2 * dx * dy / (dx*dx + dy*dy)
        
        resX0  = round(a * (px0 - xInit) + b*(py0 - yInit) + xInit);
        # resY0  = round(b * (px0 - xInit) - a*(py0 - yInit) + yInit);
        
        
        px1=objaxis[3]
        py1=objaxis[0]
        
#        xInit = int(N_Cols/2)
#        yInit = 0
#        xFinal = int(N_Cols/2)
#        yFinal = N_Rows
#        
#        
#        dx  = xFinal - xInit
#        dy  = yFinal - yInit
        
#        a   = (dx * dx - dy * dy) / (dx * dx + dy*dy)
#        b   = 2 * dx * dy / (dx*dx + dy*dy)
        
        resX1  = round(a * (px1 - xInit) + b*(py1 - yInit) + xInit);
        # resY1  = round(b * (px1 - xInit) - a*(py1 - yInit) + yInit);
        
        
        objaxisFlipHor[1] = min([resX0,resX1])
        objaxisFlipHor[3] = max([resX0,resX1])
        
        objaxisFlipHor[0] = objaxis[0]
        objaxisFlipHor[2] = objaxis[2]
        
        # 2. Call place object function (.place_obj())
        newCoord = self.place_obj(objfullFlipHor, objroiFlipHor, objaxisFlipHor, place_row, place_col)
        
        # 3. Update coordinates 
        self.dictionary_Sprites[sprite_name][3]=newCoord[0]
        self.dictionary_Sprites[sprite_name][4]=newCoord[1]
       
        
        
    def flip_ver(self, sprite_name, place_row, place_col):
        """ Flip the sprite vertically."""

        # 1. Extract information from object dictionary (dictionary_Sprites)
        objfull=self.dictionary_Sprites[sprite_name][0]
        objroi=self.dictionary_Sprites[sprite_name][1]
        objaxis=self.dictionary_Sprites[sprite_name][2]
        
        # 2. Flip sprite and mask
        objfullFlipVer=np.flipud(objfull)
        objroiFlipVer=np.flipud(objroi)
        
        # 3. Flip borders of REC
        objaxisFlipVer = [0,0,0,0]
        N_Cols=objfull.shape[1]
        N_Rows=objfull.shape[0]
        
        px0=objaxis[1]
        py0=objaxis[0]
        
        xInit = 0
        yInit = int(N_Rows/2)
        xFinal = N_Cols
        yFinal = yInit
        
        
        dx  = xFinal - xInit
        dy  = yFinal - yInit
        
        a   = (dx * dx - dy * dy) / (dx * dx + dy*dy)
        b   = 2 * dx * dy / (dx*dx + dy*dy)
        
        # resX0  = round(a * (px0 - xInit) + b*(py0 - yInit) + xInit);
        resY0  = round(b * (px0 - xInit) - a*(py0 - yInit) + yInit);
        
        
        px1=objaxis[1]
        py1=objaxis[2]
               
        
        dx  = xFinal - xInit
        dy  = yFinal - yInit
        
        a   = (dx * dx - dy * dy) / (dx * dx + dy*dy)
        b   = 2 * dx * dy / (dx*dx + dy*dy)
        
        # resX1  = round(a * (px1 - xInit) + b*(py1 - yInit) + xInit);
        resY1  = round(b * (px1 - xInit) - a*(py1 - yInit) + yInit);
        
        
        objaxisFlipVer[0] = min([resY0,resY1])
        objaxisFlipVer[2] = max([resY0,resY1])
        
        objaxisFlipVer[1] = objaxis[1]
        objaxisFlipVer[3] = objaxis[3]
        
        # 2. Call place object function (.place_obj())
        newCoord = self.place_obj(objfullFlipVer, objroiFlipVer, objaxisFlipVer, place_row, place_col)
        
        # 3. Update coordinates 
        self.dictionary_Sprites[sprite_name][3]=newCoord[0]
        self.dictionary_Sprites[sprite_name][4]=newCoord[1]
        
        
    def play_video(self, delay):
        """ play_video(delay)                             
              Plays the video with a delay between frames.
              The delay is given in seconds.
              The video play can be controlled.
            Example:
               # Play the video with 1 second delay between frames:
               myvideo.play_video(1)
        """
        
        print("play_video(delay={})".format(delay))
        print("Press ANY key to access video commands")
        print("Press 'p' for pause and resume.")
        print("Press 'f' to forward by 1 frame.")
        print("Press 'r' to rewind by 1 frame.")
        print("Press 's' to show the frame in a new window.")
        print("Press 'q' to stop.")
        
        EMPTY=-1
        prev_key=EMPTY  # normal mode
        key=EMPTY       # normal mode
        while key!=ord('q'):
            i=0
            while (i >=0) and (i<len(self.video)):
                name='Video'
                cv2.imshow(name, self.video[i])
                i += 1
                                   
                if key==EMPTY:                    
                    n=np.round(delay*1000).astype(int)
                    key=cv2.waitKey(n)                    
                else:   
                    # Wait for an input
                    print("Frame={} Key: quit, pause, forward, rewind, show".format(i-1))                    
                    prev_key=key
                    minute_delay=60*1000
                    key=cv2.waitKey(minute_delay)
                    
                    # Implement the key.
                    if (prev_key==ord('p')) and (key==ord('p')):
                        key=EMPTY       # resume play
                    elif key==ord('p'):                        
                        i -= 1          # Do not advance the frame
                    elif key==ord('f'):
                        pass             # Let it go to the next frame
                    elif key==ord('r'):
                        i -= 2           # Back one
                    elif key==ord('s'):
                        num = "Frame={}".format(i-1)
                        plot_img(self.video[i-1], num)
                        i -= 1           # Stay here
                    elif key==ord('q'):
                        break            # Get out of the loop
                    
                                        # 'p', 'f', 'r' modes
                    

        
    def save_video(self,fps,VideoName='output'):
        """ save_video(fps, VideoName)
          saves the video in the file called VideoName.avi.
          fps specifies the number of frames-per-second. Must be greater than 1.5
        Example:
            # Saves to test1.avi at 5 frames per second.
            myvideo.save_video(5,'test1')
        """
        if fps < 1.5 :
            print('fps out of range, increase to 1.5 or larger')
            sys.exit(0)
        
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
        outObj = cv2.VideoWriter('{}.avi'.format(VideoName),
                                 fourcc, 
                                 fps, 
                                 (self.num_of_cols,self.num_of_rows))
       
        for i in range(0,len(self.video)):
            frame=self.video[i]
            outObj.write(frame)

        outObj.release()
            
    def get_num_of_frames(self):
        """ get_num_of_frames()
          returns the number of video frames.
         Example:
             n=myvideo.get_num_of_frames()
             print("Num of frames = ", str(n))
        """
        
        return(len(self.video))        

    def get_distance(self,sprite_name):
        """ get_distance()
          returns the pythagorean distance traveled by the sprite .
         Example:
             distance_B1=myvideo.get_distance('B1')
             print("Distance traveled = ", str(distance_B1))
        """
        
        distance_moved=self.dictionary_Sprites[sprite_name][5]        
        return(distance_moved) 

    def show_back(self,back_name):
        """ show_back(back_name)
              displays the background image 
              given by back_name.
        Example:
           ... initialize myvideo using vid()
           
           import aolme2
           bac=load_img("backgroundMario.jpg")
           myvideo.set_back('back1', bac) 
           myvideo.show_back('back1')
        """
        
        print("show_back({})".format(back_name))
        try:
            im=self.dictionary_Backgrounds[back_name]  
            str = "Background image: {}".format(back_name)
            plot_img(im, str)
        except:
            print("ERROR: I cannot display the background image")
            print("SUGGESTION: Check back_name={}".format(back_name))
            sys.exit(0)
    
    
    def show_sprite(self,sprite_name):
        """ show_sprite(sprite_name)
              displays the sprite named sprite_name. 
         Example:
            ... initialize myvideo using vid()
            ... initialize and save the sprite into
            ...   the file B1.pickle.
            
            myvideo.set_sprite('B1')
            myvideo.show_sprite('B1')
        """
        
        print("show_sprite({})".format(sprite_name))
        try:
            objfull=self.dictionary_Sprites[sprite_name][0]
            objroi=self.dictionary_Sprites[sprite_name][1]
            
            sprite_size_rows=objfull.shape[0]
            sprite_size_cols=objfull.shape[1]
            
            
            maskObj=np.zeros((sprite_size_rows,sprite_size_cols,3),  dtype=np.uint8)
            maskObj[:,:,0]=objroi
            maskObj[:,:,1]=objroi
            maskObj[:,:,2]=objroi
            
            sprite_no_background = np.ones((sprite_size_rows,sprite_size_cols,3),  dtype=np.uint8)
            sprite_no_background=sprite_no_background*255
            np.copyto(sprite_no_background, objfull, where=(maskObj>0))
            
            img_title="Sprite: {}".format(sprite_name)
            plot_img(sprite_no_background, img_title)
    
        except:
            print("ERROR: I cannot show the sprite!")
            print("SUGGESTION: Check sprite_name={}".format(sprite_name))
            sys.exit(0)
    
    
    def show_last_frame(self):
        """ show_last_frame():
              displays the last frame in the video.
        """
        
        print("show_last_frame()")
        try:
            im=self.video[-1]
            plot_img(im,"Last Video Frame")
        except:
            print("ERROR: Cannot show the last frame!")  
            print("SUGGESTION: Make sure to save frames in your video")
            print("\n")
            sys.exit(0)
            
    def draw_path(self, sprite_name):
        """ draw_path():
                draw a blue line of 5px as the path of the sprite 
        """
        print("draw_path()")
        try: 
            path_coordinates = self.dictionary_Sprites[sprite_name][7]        
            for i in range(len(path_coordinates)-1):
               im=self.video[-1]
               im = cv2.line(im,path_coordinates[i],path_coordinates[i+1],(255,0,0),5)
            plot_img(im,"Path of {}".format(sprite_name))
        except:
            print("ERROR: Cannot show the path of the sprite!")  
            print("SUGGESTION: Make sure you enabled 'Trace' in >.sprite_move()")
            print("\n")
            sys.exit(0)
            
    def get_path(self, sprite_name):
        """ get_path():
            returns the path to study the TSP.
        """
        
        try: 
            coords = self.dictionary_Sprites[sprite_name][7]
            nodes = []
            for i in range(len(coords)-1):
                col, row = coords[i]
                nodes.append([row, col])
            col, row = coords[i+1]
            nodes.append([row,col])
        except:
            print("ERROR: Cannot get the path of the sprite!")  
            print("SUGGESTION: Make sure you enabled 'Trace' in >.sprite_move()")
            print("\n")
            sys.exit(0)
            
        return(nodes)
        
        