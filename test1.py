
import  numpy as np
import	cv2
from matplotlib import pyplot as plt

img = cv2.imread('test1.jpg')

#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
k = cv2.waitKey(0)

if k == 27:
	cv2.destroyAllWindows()
elif	k == ord('s'):
	cv2.imwrite('test1_wr.png',img)
	cv2.destroyAllWindows()
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
# plt.show()
