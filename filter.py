import cv2
import numpy as np 
from matplotlib import pyplot as plt

img = cv2.imread('test1_wr.png')

kernel = np.ones((7, 7), np.float32)/49

# dst = cv2.filter2D(img, -1, kernel)
dst = cv2.blur(img,(7,7))
gas = cv2.GaussianBlur(img, (7,7),0)
med = cv2.medianBlur(img, 7)

# cv2.imshow('Test1',img)
# cv2.waitKey(0)
# # cv2.destroyAllWindow()

plt.subplot(221), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(gas), plt.title('Gaussian')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(gas), plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.show()


