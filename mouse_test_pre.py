# -*- coding: utf-8 -*-

import cv2
import numpy as np


drawing = False
mode = True
ix, iy = -1, -1


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing:
            if mode:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
            else:
                cv2.circle(img, (x, y), 6, (0, 0, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 0), -1)
        else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_circle)

while (1):
    cv2.imshow('Image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
