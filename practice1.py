import cv2 as cv 

img = cv.imread('images/sample.jpg')

cv.imshow('sample', img)

cv.waitKey(0)