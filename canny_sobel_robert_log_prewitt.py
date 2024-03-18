import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the input image
img = cv2.imread('rabbit.jpg', cv2.IMREAD_GRAYSCALE)

# Canny edge detection
canny_edges = cv2.Canny(img, 100, 200)

# Robert edge detection
robert_x = cv2.filter2D(img, cv2.CV_64F, np.array([[-1, 0], [0, 1]]))
robert_y = cv2.filter2D(img, cv2.CV_64F, np.array([[0, -1], [1, 0]]))
robert_edges = np.sqrt(robert_x**2 + robert_y**2)

# Sobel edge detection
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_edges = np.sqrt(sobel_x**2 + sobel_y**2)

# Prewitt edge detection
prewitt_x = cv2.filter2D(img, cv2.CV_64F, np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]))
prewitt_y = cv2.filter2D(img, cv2.CV_64F, np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]]))
prewitt_edges = np.sqrt(prewitt_x**2 + prewitt_y**2)

# LoG (Laplacian of Gaussian) edge detection
gaussian_blur = cv2.GaussianBlur(img, (3, 3), 0)
log_edges = cv2.Laplacian(gaussian_blur, cv2.CV_64F)

plt.figure(figsize=(20, 10))
plt.subplot(2, 3, 1),plt.imshow(img, cmap='gray')
plt.title('Original Image'),plt.axis('off')

plt.subplot(2, 3, 2),plt.imshow(canny_edges, cmap='gray')
plt.title('Canny Edge Detection'),plt.axis('off')


plt.subplot(2, 3, 3)
plt.imshow(robert_edges, cmap='gray')
plt.title('Robert Edge Detection'),plt.axis('off')

plt.subplot(2, 3, 4),plt.imshow(sobel_edges, cmap='gray')
plt.title('Sobel Edge Detection'),plt.axis('off')

plt.subplot(2, 3, 5),plt.imshow(prewitt_edges, cmap='gray')
plt.title('Prewitt Edge Detection'),plt.axis('off')

plt.subplot(2, 3, 6),plt.imshow(log_edges, cmap='gray')
plt.title('Log Edge Detection'),plt.axis('off')

plt.show()
