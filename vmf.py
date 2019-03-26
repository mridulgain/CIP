#vector median filter
import cv2
import sys
import array 
import numpy as np

def euclidian_dist(v1, v2):
    #calculating euclidian distance between two vectors v1, v2
    dist = 0
    for i in range(3):
        x = int(v1[i])
        y = int(v2[i])
        dist += (x - y)**2
    return dist**0.5

def canberra_dist(v1, v2):
    #calculating canberra distance between two vectors v1, v2
    dist = 0
    for i in range(3):
        x = int(v1[i])
        y = int(v2[i])
        if x == 0 and y == 0:
            dist += 0
        else:
            dist += abs(x-y)/(x+y)
    return dist

def manhattan_dist(v1, v2):
    #calculating manhattan distance between two vectors v1, v2
    dist = 0
    for i in range(3):
        x = int(v1[i])
        y = int(v2[i])
        if x == 0 and y == 0:
            dist += 0
        else:
            dist += abs(x-y)
    return dist

def get_median(win_vectors):
    #calculate the median 
    dist = np.zeros(shape = (9,9))
    for i in range(9):
        for j in range(i, 9):
            #dist[i][j] = euclidian_dist(win_vectors[i], win_vectors[j])
            dist[i][j] = canberra_dist(win_vectors[i], win_vectors[j])
            dist[j][i] = dist[i][j]
    min_dist = sum(dist[0])
    median = win_vectors[0]
    for i in range(1, 9):
        temp = sum(dist[i])
        if temp < min_dist:
            min_dist = temp
            median = win_vectors[i]
    return median
    
def vmf():
    #win_size = 3
    img = cv2.imread(sys.argv[1])
    hight, width = img.shape[:2]
    output_img = np.copy(img)
    print("image resolution :", width ,"x" ,hight)
    for row in range(1,hight-1):
        print("working on row:", row, end = "\r")
        for col in range(1,width-1):
            #calculate lowest median
            win_vectors = []
            for win_r in range(row-1,row+2):
                for win_c in range(col-1, col+2):
                    win_vectors.append(img[win_r][win_c])
            output_img[row][col] = get_median(win_vectors)
    cv2.imshow('input', img)
    cv2.imshow('output', output_img)
    cv2.waitKey()
    cv2.imwrite("vmf_euclidian_.ppm", output_img)
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("error : please provide file name as command line argument")
        print("try : python", sys.argv[0], "<image_file_name>")
    else:
        #applying median filter
        vmf()