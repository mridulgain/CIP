#RGB ranging
import cv2
import numpy as np
def calculate_range(c, bw):
    l = (c - bw) if c - bw >= 0 else 0
    r = (c + bw) if c + bw <= 255 else 255 
    return l,r
def colour_rangingRGB(r_c, r_bw, g_c, g_bw, b_c, b_bw):
    img = cv2.imread("./test_images/orchid.ppm")
    input_img = np.copy(img)
    print("image resolution :", width, hight)
    for color_comp in range(3):
        if(color_comp == 0):#blue
            l, r = calculate_range(b_c, b_bw)
        elif(color_comp == 1):#green
            l, r = calculate_range(g_c, g_bw)
        else:           #red
            l, r = calculate_range(r_c, r_bw)
        print("range :" , l , "to" ,r, end="\r")
        for row in range(hight):
            for col in range(width):                
                if img[row][col][color_comp] < l or img[row][col][color_comp] > r:
                    img[row][col][color_comp] = 0
    cv2.imshow("Input", input_img)
    cv2.imshow("Output", img)
    cv2.waitKey(0)

if __name__ == '__main__':
    colour_rangingRGB(0, 255, 0, 0, 0, 255)