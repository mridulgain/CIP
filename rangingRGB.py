#RGB ranging
import sys
import cv2
import numpy as np
def calculate_range(c, bw):
    l = (c - bw) if c - bw >= 0 else 0
    r = (c + bw) if c + bw <= 255 else 255 
    return l,r
def colour_rangingRGB(img, r_c, r_bw, g_c, g_bw, b_c, b_bw):
    try:
        input_img = np.copy(img)
        height, width = img.shape[:2]
        print("image resolution :", width, height)
        for color_comp in range(3):
            if(color_comp == 2):#blue
                l, r = calculate_range(b_c, b_bw)
                print("For Blue: ")
            elif(color_comp == 1):#green
                l, r = calculate_range(g_c, g_bw)
                print("For Green: ")
            else:           #red
                l, r = calculate_range(r_c, r_bw)
                print("For red: ")
            print("Retaining values in [", l,r, "]")
            for row in range(height):
                for col in range(width):                
                    if img[row][col][color_comp] < l or img[row][col][color_comp] > r:
                        img[row][col][color_comp] = 0
        cv2.imshow("Input", cv2.cvtColor(input_img, cv2.COLOR_RGB2BGR))
        cv2.imshow("Output", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
        cv2.waitKey(0)
    except AttributeError:
        print("Invalid file. Please check the file name you have entered")

if __name__ == '__main__':
    #applying RGV ranging
    try:
        img = cv2.imread(sys.argv[1])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        colour_rangingRGB(img, 0, 0, 70, 200, 0, 0)
    except IndexError:
        print("error : please provide file name as command line argument")
        print("try : python", sys.argv[0], "<image_file_name>")