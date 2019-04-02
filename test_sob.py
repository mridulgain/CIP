import cv2
import numpy as np

sobelX = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
sobelY = sobelX.T

imgoriginal = cv2.imread("./test_images/orchid.ppm") 
imgoriginal = cv2.cvtColor(imgoriginal, cv2.COLOR_BGR2GRAY)
imgh = cv2.filter2D(imgoriginal, -1, sobelY)
imgv = cv2.filter2D(imgoriginal, -1, sobelX)
#imgboth = (imgv**2 + img**2)**0.5
cv2.imshow("v_edge", imgv)
cv2.imshow("h_edge", imgh)
#cv2.imshow("v_edge", imgv)
cv2.waitKey()