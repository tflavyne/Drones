import numpy
import cv2

# video = cv2.VideoCapture("vid.mp4")
# fourcc = cv2.VideoWriter_fourcc(*"mp4v")
# width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
# output = cv2.VideoWriter('SimpleColorThresholder.mp4', fourcc, 25, (width, height))

import numpy
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    #lb = lower bound orange & ub = higherbound orange
    lb = np.array([212, 120, 0])
    ub = np.array([209, 122, 9])

    mask = cv2.inRange(hsv, lb, ub)

    result = cv2.bitwise_and("Vid.mp4", frame, mask=mask)

    cv2.imshow("Vid.mp4", frame)

    cap.relase()
