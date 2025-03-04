import cv2
import numpy as np 

def draw_circle(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDOWN:
	# events: L:left button down;up;DBLCLK:double click
		cv2.circle(img,(x,y),10,(125,125,125),-1)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while (1):
	cv2.imshow('image',img)
	if cv2.waitKey(20)&0xFF == 27:
		break
cv2.destroyAllWindows()