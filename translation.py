import cv2
import numpy as np 

image = cv2.imread("sample.jpg")

tx, ty = 100, 50 

translation_matrix = np.float32([
    [1,0,tx],
    [0,1,ty]
])

height, width = image.shape[:2]

translated_image = cv2.warpAffine(image,translation_matrix, (height, width))

cv2.imshow("translated image", translated_image)

cv2.waitKey(0)
cv2.imwrite("translated.png", translated_image)
print("Saved as rotated.png in the same folder.")
