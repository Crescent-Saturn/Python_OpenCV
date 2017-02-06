import cv2
import numpy as np

img = cv2.imread('cv.jpg')

img2 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

# h, w = img.shape[:2]

# res = cv2.resize(img, (2*h, 2*w), interpolation=cv2.INTER_CUBIC)

# cv2.imshow('Original', img)
cv2.imshow('Half', img2)
# cv2.imshow('Half', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
