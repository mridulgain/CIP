#vector edge detector for color image
import cv2
import sys
import array 
import numpy as np

def ved_color(img):
    try:
        win_size = 3
        hight, width = img.shape[:2]
        output_img = np.copy(img)
        print("image resolution :", width ,"x" ,hight)
        mask_x = np.array([
            [-1, 0, 1],
            [-1, 0, 1],
            [-1, 0, 1]
        ])
        mask_y = mask_x.T
        for row in range(hight-2):
            print("working on row:", row, end = "\r")
            for col in range(width-2):
                gx = 0
                gy = 0
                for win_r in range(win_size):
                    for win_c in range(win_size):
                            gy += img[row + win_r][col + win_c] * mask_y[win_r][win_c]
                            gx += img[row + win_r][col + win_c] * mask_x[win_r][win_c]
                g = abs(gx) + abs(gy)
                for i in range(3):
                    if g[i] > 255:
                        g[i] = 255
                output_img[row+1][col+1] = g
        cv2.imshow('input', img)
        cv2.imshow('output', output_img)
        cv2.waitKey()
    except AttributeError:
        print("Invalid file. Please check the file name you have entered")



if __name__ == '__main__':
    #applying edge detection
    try:
        img = cv2.imread(sys.argv[1])
        ved_color(img)
    except IndexError:
        print("error : please provide file name as command line argument")
        print("try : python", sys.argv[0], "<image_file_name>")