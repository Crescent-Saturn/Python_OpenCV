import cv2
import numpy as np


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 10, (0, 255, 0), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Circle')
cv2.setMouseCallback('Circle', draw_circle)

while (1):
    cv2.imshow('Circle', img)
    if cv2.waitKey(20) == 27:
        break

cv2.destroyAllWindows()
