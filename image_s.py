# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread('test1.jpg')

px = img[100, 100]
print(px)

blue = img[100, 100, 0]
print(blue)

print(img.shape, img.size)
print(img.dtype)

cv2.imshow('Img', img)
cany = cv2.Canny(img, 200, 300)
cv2.imshow('cany', cany)
cv2.waitKey(0)
cv2.destroyAllWindows()
  
