import cv2

# LOADING IMAGE

img = cv2.imread('onepiece.jpg')

print(img)

cv2.imshow('Using CV2',img)
cv2.waitKey(5000)

