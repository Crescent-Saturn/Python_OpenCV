# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

cv2.rectangle(img, (345, 123), (505, 450), (0, 255, 0), 3)

cv2.imshow('Img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
