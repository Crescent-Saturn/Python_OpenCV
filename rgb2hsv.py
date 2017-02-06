import cv2
import numpy as np

cap = cv2.VideoCapture(0)


def fdhsv(color):
    # function to find hsv value of BGR
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

    return hsv_color


r = np.uint8([[[0, 0, 255]]])
g = np.uint8([[[0, 255, 0]]])
b = np.uint8([[[255, 0, 0]]])



while (1):

    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_r = np.array([0, 100, 100])
    upper_r = np.array([10, 255, 255])

    mask_r = cv2.inRange(hsv, lower_r, upper_r)

    res_r = cv2.bitwise_and(frame, frame, mask=mask_r)

    cv2.imshow('Frame', frame)
    # cv2.imshow('Mask', mask)
    cv2.imshow('Res', res_r)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
