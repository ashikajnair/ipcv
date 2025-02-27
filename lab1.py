import numpy as np 
import cv2

image = cv2.imread("img.jpg")
cv2.imshow("Original Image", image)
cv2.waitKey(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)

resized_image = cv2.resize(image, (1700, 500))
cv2.imshow('Resized', resized_image)
cv2.waitKey(0)

Gaussian = cv2.GaussianBlur(image, (7, 7), 0) 
cv2.imshow('Gaussian Blurring', Gaussian) 
cv2.waitKey(0) 

median = cv2.medianBlur(image, 5) 
cv2.imshow('Median Blurring', median) 
cv2.waitKey(0) 

border_image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value = 0)
cv2.imshow('Border Image', border_image) 
cv2.waitKey(0)

reflect_image = cv2.copyMakeBorder(image, 100, 100, 50, 50, cv2.BORDER_REFLECT) 
cv2.imshow('Reflect Image', reflect_image) 
cv2.waitKey(0)

rotate_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated Image', rotate_image) 
cv2.waitKey(0)

cropped_image = image[80:280, 150:330]
cv2.imshow("Cropped Image", cropped_image)
cv2.waitKey(0)

height, width = image.shape[:2] 
quarter_height, quarter_width = height / 4, width / 4
T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]]) 
img_translation = cv2.warpAffine(image, T, (width, height)) 
cv2.imshow('Translation', img_translation) 
cv2.waitKey() 
  
cv2.destroyAllWindows()
