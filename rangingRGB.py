import matplotlib.pyplot as plt
import cv2
def calculate_range(c, bw):
    l = (c - bw) if c - bw >= 0 else 0
    r = (c + bw) if c + bw <= 255 else 255 
    return l,r
def colour_rangingRGB(r_c, r_bw, g_c, g_bw, b_c, b_bw):
    img = cv2.imread("./test images/orchid.ppm")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hight, width = img.shape[:2]
    print("image resolution :", width, hight)
    for hue in range(3):
        if(hue == 0):#red
            l, r = calculate_range(r_c, r_bw)
        if(hue == 1):#green
            l, r = calculate_range(g_c, g_bw)
        if(hue == 2):
            l, r = calculate_range(b_c, b_bw)
        print("range :" , l , "to" ,r)
        for row in range(hight):
            for col in range(width):
                """ if(hue != 0):
                    img[row][col][hue] = 0 """
                if img[row][col][hue] < l or img[row][col][hue] > r:
                    img[row][col][hue] = 0
    plt.imshow(img)
    plt.show()

if __name__ == '__main__':
    colour_rangingRGB(0, 0, 0, 255, 0, 0)