import cv2
import numpy as np
import matplotlib.pyplot as plt
def rgb2hsv(rgb):
    color_rgb = np.uint8([[rgb]])
    #viewColourRGB(color_rgb)
    color_hsv = cv2.cvtColor(color_rgb, cv2.COLOR_RGB2HSV)
    #viewColourHSV(color_hsv)
    return color_hsv

def hsv2rgb(hsv):
    color_hsv = np.uint8([[hsv]])
    #viewColourHSV(color_hsv)
    color_rgb = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2RGB)
    #viewColourRGB(color_rgb)
    return color_rgb

def viewColourRGB(rgb):
    color_rgb = np.uint8([[rgb]])
    plt.imshow(color_rgb)
    plt.show()

def viewColourHSV(hsv):
    color_hsv = np.uint8([[hsv]])
    img = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2RGB)
    plt.imshow(img)
    plt.show()

if __name__ == "__main__":
    """ rgb = [255,255,255]
    print(rgb, "->", rgb2hsv(rgb))
    viewColourRGB(rgb) """
    hsv = [10,255,255]
    print(hsv, "->", hsv2rgb(hsv))
    viewColourHSV(hsv)