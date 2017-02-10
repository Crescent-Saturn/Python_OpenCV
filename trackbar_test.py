# -*- coding: utf-8 -*-

import cv2
import numpy as np


def nothing():
    pass


img = np.zeros((480, 640, 3), np.uint8)
cv2.namedWindow('Color')

cv2.createTrackbar('R', 'Color', 0, 255, nothing)
cv2.createTrackbar('G', 'Color', 0, 255, nothing)
cv2.createTrackbar('B', 'Color', 0, 255, nothing)

switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch, 'Color', 0, 1, nothing)

while (1):
    cv2.imshow('Color', img)
    k = cv2.waitKey(1) &0xFF
    if k == 27:
        break

    r = cv2.getTrackbarPos('R', 'Color')
    g = cv2.getTrackbarPos('G', 'Color')
    b = cv2.getTrackbarPos('B', 'Color')
    s = cv2.getTrackbarPos(switch, 'Color')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()