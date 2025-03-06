import numpy as np 
import cv2

image = cv2.imread("img.jpg")
cv2.imshow("Original Image", image)
cv2.waitKey(0)

resized_image = cv2.resize(image, (1000, 700))
cv2.imshow('Resized image', resized_image)
cv2.waitKey(0)

rotate_image = cv2.rotate(image, cv2.ROTATE_180)
cv2.imshow('Rotated Image', rotate_image) 
cv2.waitKey(0)

# Store height and width of the image 
height, width = image.shape[:2] 

quarter_height, quarter_width = height / 4, width / 4

T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]]) 

# We use warpAffine to transform 
# the image using the matrix, T 
img_translation = cv2.warpAffine(image, T, (width, height)) 

cv2.imshow('Translation of Image', img_translation) 
cv2.waitKey()

cv2.destroyAllWindows()
