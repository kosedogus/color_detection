import numpy as np
import cv2

def get_limits(color):
    c = np.uint8([[[color[0], color[1], color[2]]]])
    hsv = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    h = hsv[0][0][0]
    s = hsv[0][0][1]
    v = hsv[0][0][2]
    lower = np.array([h-10, s-100, v-100])
    upper = np.array([h+10, s+255, v+255])
    return lower, upper

