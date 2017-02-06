import cv2
import numpy as np

img = cv2.imread('cv.jpg')
img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

rows, cols = img.shape[:2]

m = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, m, (cols, rows))

cv2.imshow('img', dst)
cv2.imshow('orig', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
