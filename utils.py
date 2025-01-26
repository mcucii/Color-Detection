import cv2
import numpy as np

def getColorBounds(color) :
    hsvC = cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]
    
    lowerBound = max(hue-10,0), 100,100
    upperBound = min(hue+10,180), 255,255

    lowerBound = np.array(lowerBound, dtype=np.uint8)
    upperBound = np.array(upperBound, dtype=np.uint8)
    return lowerBound, upperBound
