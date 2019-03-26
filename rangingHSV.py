import cv2
import sys
import numpy
def calculate_range(c, bw):
    l = (c - bw) if c - bw >= 0 else 0
    r = (c + bw) if c + bw <= 179 else 179 
    return l,r
def colour_rangingHSV(h_c, h_bw, s_c, v_c):
    img = cv2.imread(sys.argv[1])
    hight, width = img.shape[:2]
    input_img = numpy.copy(img)
    print("image resolution :", width ,"x" ,hight)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    l, r = calculate_range(h_c, h_bw)
    for row in range(hight):
        print("working on row :",row , end="\r")
        for col in range(width):
            spec = img[row][col]
            #hue
            if(spec[0]<l or spec[0]>r):
                spec[0] = 0
            #saturation
            if spec[1] <= s_c :
                spec[1] = 0
            #value
            if spec[2] <= v_c :
                spec[2] = 0
            img[row][col] = spec
    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    cv2.imshow('input', input_img)
    cv2.imshow('output', img)
    cv2.waitKey(0)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("error : please provide file name as command line argument")
        print("try : python", sys.argv[0], "<image_file_name>")
    else:
        #extracting green
        colour_rangingHSV(0, 22, 150, 50)