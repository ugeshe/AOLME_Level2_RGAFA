
import random
# Wenjing image threshold module
from thresholds2 import threshold, comb_thr


def get_img_object_center(img, rth, gth, bth):
    """
    Returns centroid of the object detected using
    color thresholds.
    """

    thr_obj               = threshold(img)
    thr_obj.sel_color_comp('red')
    RedRange              = thr_obj.ThreshRange (rth[0], rth[1])
    thr_obj.sel_color_comp('green')
    GreenRange            = thr_obj.ThreshRange (gth[0], gth[1])
    thr_obj.sel_color_comp('blue')
    BlueRange             = thr_obj.ThreshRange (bth[0], bth[1])
    (obj_center, ang, img, max_area) = comb_thr(img, BlueRange, GreenRange, RedRange, 'Vision', 90, 'test').returnResults()
    if (len(obj_center) == 0):
        x = random.randint(0,int(img.shape[1]/2))
        y = random.randint(0,int(img.shape[0]/2))
    else:
        x = obj_center[0]
        y = obj_center[1]


    return x,y, max_area

def show_RGB_hist(img, rgb_values ):
     """
     Show the image and the RGB histograms.
     """
     th = threshold(img)
     th.show_hist_with_th(rgb_values)

