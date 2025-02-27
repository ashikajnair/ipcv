import cv2
import matplotlib.pyplot as plt

def divide_image_into_quadrants(image):
    height, width = image.shape[:2]

    mid_x, mid_y = int(width / 2), int(height / 2) 

    top_left = image[:mid_y, :mid_x]
    top_right = image[:mid_y, mid_x:]
    bottom_left = image[mid_y:, :mid_x]
    bottom_right = image[mid_y:, mid_x:]

    return top_left, top_right, bottom_left, bottom_right

# Example usage
img = cv2.imread('img.jpg')  # Use the correct path

# Divide the image into quadrants
quadrants = divide_image_into_quadrants(img)

# Access individual quadrants
top_left = quadrants[0]
top_right = quadrants[1]
bottom_left = quadrants[2]
bottom_right = quadrants[3]

# Convert BGR to RGB for displaying with matplotlib
top_left_rgb = cv2.cvtColor(top_left, cv2.COLOR_BGR2RGB)
top_right_rgb = cv2.cvtColor(top_right, cv2.COLOR_BGR2RGB)
bottom_left_rgb = cv2.cvtColor(bottom_left, cv2.COLOR_BGR2RGB)
bottom_right_rgb = cv2.cvtColor(bottom_right, cv2.COLOR_BGR2RGB)

# Display images using matplotlib
plt.figure(figsize=(6, 6))

# Show the top-left quadrant
plt.subplot(2, 2, 1)
plt.imshow(top_left_rgb)
# plt.title('Top Left')
plt.axis('off')

# Show the top-right quadrant
plt.subplot(2, 2, 2)
plt.imshow(top_right_rgb)
# plt.title('Top Right')
plt.axis('off')

# Show the bottom-left quadrant
plt.subplot(2, 2, 3)
plt.imshow(bottom_left_rgb)
# plt.title('Bottom Left')
plt.axis('off')

# Show the bottom-right quadrant
plt.subplot(2, 2, 4)
plt.imshow(bottom_right_rgb)
# plt.title('Bottom Right')
plt.axis('off')

# Show the plot with all quadrants
plt.tight_layout()
plt.show()
