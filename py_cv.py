#from cv2.cv import *
import numpy as np  
import cv2

#img = LoadImage("maxresdefault.jpg")
im2 = cv2.imread("maxresdefault.jpg")

cv2.namedWindow("Image")   
cv2.imshow("Image",im2)
#NamedWindow("opencv")
#ShowImage("opencv",img)
cv2.waitKey(0)
cv2.destroyAllWindows()  

#```
#img = cv2.imread("maxresdefault.jpg")  
#emptyImage = np.zeros(img.shape, np.uint8)  
  
#emptyImage2 = img.copy()  
  
#emptyImage3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
#emptyImage3[...]=0  
  
#cv2.imshow("EmptyImage", emptyImage)  
#cv2.imshow("Image", img)  
#```
