import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('image2.jpg', cv2.IMREAD_GRAYSCALE)

# Enhance contrast using Histogram Equalization
equalized_image = cv2.equalizeHist(image)

# 2. Segment the image using a thresholding technique
_, segmented_image = cv2.threshold(equalized_image, 127, 255, cv2.THRESH_BINARY)

# Plot the results using matplotlib to visualize the effect
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Enhanced Image (Histogram Equalization)")
plt.imshow(equalized_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Segmented Image (Thresholding)")
plt.imshow(segmented_image, cmap='gray')
plt.axis('off')

histr = cv2.calcHist([image],[0],None,[256],[0,256])
histr1 = cv2.calcHist([equalized_image],[0],None,[256],[0,256])
histr2 = cv2.calcHist([segmented_image],[0],None,[256],[0,256])
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.title("histogram of original Image")
plt.imshow(histr)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("histogram of Enhanced Image")
plt.imshow(histr1)
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("histogram of Segmented Image")
plt.imshow(histr2)
plt.axis('off')

plt.tight_layout()
plt.show()
