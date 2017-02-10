# -*- coding: utf-8 -*-

import cv2
import numpy as np

draw = False
mode = True


def draw_circle(event, x, y, flags, param):
    r = cv2.getTrackbarPos('R', 'Image')
    g = cv2.getTrackbarPos('G', 'Image')
    b = cv2.getTrackbarPos('B', 'Image')
    color = [b, g, r]

    global ix, iy, mode, draw
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if draw:
            if mode:
                cv2.circle(img, (x, y), 3, color, 2)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False


def nothing():
    pass


img = np.zeros((480, 640, 3), np.uint8)
color = np.zeros((255, 3))

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_circle)

cv2.createTrackbar('R', 'Image', 0, 255, nothing)
cv2.createTrackbar('G', 'Image', 0, 255, nothing)
cv2.createTrackbar('B', 'Image', 0, 255, nothing)


while (1):
    cv2.imshow('Image', img)
    k = cv2.waitKey(1) & 0xFF

    if k == 27:
        break

cv2.destroyAllWindows()
