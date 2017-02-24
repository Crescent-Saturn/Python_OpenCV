import cv2
from matplotlib import pyplot as plt 

img = cv2.imread('test1.jpg')

blt = cv2.bilateralFilter(img, 9, 75,75)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blt), plt.title('Bilateral')
plt.xticks([]), plt.yticks([])
plt.show()
