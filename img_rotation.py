import cv2
import numpy as np

img = cv2.imread('opencv-logo-white.png')
rows, cols = img.shape[:2]

M = cv2.getRotationMatrix2D((rows/2, cols/2), 90, 0.6)

dst = cv2.warpAffine(img, M, (2 * cols, 2 * rows))

cv2.imshow('Ori', img)
cv2.imshow('Rot', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
