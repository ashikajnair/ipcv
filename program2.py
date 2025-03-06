import numpy as np 
import cv2

#---ORIGINAL IMAGE---
image = cv2.imread("img.jpg")
cv2.imshow("Original Image", image)
cv2.waitKey(0)


#---SCALING OF IMAGE---
resized_image = cv2.resize(image, (1000, 700))
cv2.imshow('Resized image', resized_image)
cv2.waitKey(0)


#---ROTATION OF IMAGE---

#180 ROTATION
rotate_image = cv2.rotate(image, cv2.ROTATE_180)
cv2.imshow('Rotated Image 180', rotate_image) 
cv2.waitKey(0)

#90C ROTATION
rotate_image90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated Image 90C', rotate_image90) 
cv2.waitKey(0)

#90A ROTATION
rotate_image90A = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('Rotated Image 90A', rotate_image90A) 
cv2.waitKey(0)

#---TRANSLATION OF IMAGE---

# Store height and width of the image 
height, width = image.shape[:2] 

#QUARTER HEIGHT
quarter_height, quarter_width = height / 4, width / 4

T1 = np.float32([
    [1, 0, quarter_width], 
    [0, 1, quarter_height]
    ])

# We use warpAffine to transform 
# the image using the matrix, T 
img_translation = cv2.warpAffine(image, T1, (width, height)) 
cv2.imshow('Translation of Image QUARTER', img_translation) 
cv2.waitKey()

T2 = np.float32([
	[1, 0, 25],
	[0, 1, 50]
])  #shift an image 25 pixels to the right and 50 pixels down

img_translation = cv2.warpAffine(image, T2, (width, height)) 
cv2.imshow('Translation of Image 1', img_translation) 
cv2.waitKey()

T3 = np.float32([
	[1, 0, -7],
	[0, 1, -23]
])  #shift an image 7 pixels to the left and 23 pixels up
img_translation = cv2.warpAffine(image, T3, (width, height)) 
cv2.imshow('Translation of Image 2', img_translation) 
cv2.waitKey()

cv2.destroyAllWindows()
