import cv2
import numpy as np

src = cv2.imread('cow.jpg', 0)
kernel = np.ones((9, 9), np.uint8)

grad = cv2.morphologyEx(src, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(src, cv2.MORPH_TOPHAT, kernel)
# tophat == src - morph_opening

blackhat = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel)
# blackhat  == src - morph_closing

cv2.imshow('Orig', src)
cv2.imshow('Gradient', grad)
cv2.imshow('tophat', tophat)
cv2.imshow('Blackhat', blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
