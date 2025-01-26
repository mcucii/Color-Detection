import cv2
from PIL import Image
from utils import getColorBounds


yellow = [0, 255, 255]
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    if not ret:
        print('no camera input')
        break

    hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerBound, upperBound = getColorBounds(color=yellow)

    mask = cv2.inRange(hsvImg, lowerBound, upperBound)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    # cv2.drawContours(frame, contours, -1, (0,255,0), 10)

    for contour in contours:
        if cv2.contourArea(contour) > 50:  # ignore small areas
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 5)
      

  
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()