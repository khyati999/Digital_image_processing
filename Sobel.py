import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('rabbit.jpg', cv2.IMREAD_GRAYSCALE)

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
edges = np.sqrt(sobel_x**2 + sobel_y**2)
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1),plt.imshow(img, cmap='gray')
plt.title('Original Image'),plt.axis('off')


plt.subplot(1, 2, 2),plt.imshow(edges, cmap='gray')
plt.title('Sobel Edge Detection'),plt.axis('off')

plt.show()
