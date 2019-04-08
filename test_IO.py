import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("./test.ppm")
hight, width = img.shape[:2]
cv2.imshow("input", img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(len(img))
print(len(img[0]))
print(type(img[0][0]))
#hist = np.histogram(img, bins=256, range=(0,256))
cv2.imshow("output", img)
cv2.waitKey()
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.imwrite("test.ppm", img)
