import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudoku.png', 0)
img = cv2.medianBlur(img, 5)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

titles = ['Original', 'Global (v=127)', 'Adap Mean', 'Adap Gaussian']

imgs = [img, th1, th2, th3]

for i in xrange(4):
    plt.subplot(2, 2, i + 1), plt.imshow(imgs[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
