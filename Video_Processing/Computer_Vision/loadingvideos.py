import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('reading webcam',frame)
    # print frame
    
    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

