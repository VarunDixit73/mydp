import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv.cornerHarris(gray,2,3,0.04)
    dst = cv.dilate(dst,None)
    # Threshold for an optimal value, it may vary depending on the image.
    frame[dst>0.01*dst.max()]=[0,0,255]
    cv.imshow('dst',frame)
    if cv.waitKey(1) & 0xff == 27:  #esc to quit
        break
cap.release()
cv.destroyAllWindows()
