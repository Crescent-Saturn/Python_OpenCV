import cv2
import numpy as np

img = cv2.imread('cow.jpg', 0)
kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1)
dilate = cv2.dilate(img, kernel, iterations=1)

# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# closiing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Orig', img)
cv2.imshow('Erode', erosion)
cv2.imshow('Dilate', dilate)

# cv2.imshow('Morph_open', opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
