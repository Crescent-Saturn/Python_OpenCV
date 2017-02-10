# -*- coding: utf-8 -*-

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()

    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)	

    cv2.imshow('Capture', frame)  # or gray
    if cv2.waitKey(1) & 0xFF == ord('q'):  #&0xFF is for 64bit sys
        break

cap.release()
cv2.destroyAllWindows()
