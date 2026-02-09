import cv2
import numpy as np

image = cv2.imread("sample.jpg")

height, width = image.shape[:2]
center = (width // 2, height // 2)

angle = 45
scale = 1.0

rotate_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotate_image = cv2.warpAffine(image, rotate_matrix, (width, height))

cv2.imshow("Rotate Image", rotate_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("rotated.png", rotate_image)
print("Saved as rotated.png in the same folder.")
