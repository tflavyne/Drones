import cv2
import numpy as np
import scipy.signal
import matplotlib
import pylot as plt

cap = cv2.VideoCapture('Vid.mp4')

while (True):

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    for i in range(3):
        template = cv2.imread('asn4 (3).png', 0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(gray, template, cv2.TM_SQDIFF)

       min_val, max_val, min_loc = cv2.minMaxLoc(res)

        top_left = min_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        final_product = cv2.bitwise_and(bottom_right, bottom_right)

        cv2.rectangle(frame, top_left, bottom_right, 255, 1)

    cv2.imshow("Test", frame)

    if cv2.waitkey(1) & 0xFF == ord('q'):
        break

cap.release()