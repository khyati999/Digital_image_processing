import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Flower.jpg')
inverted_image = 255 - image
plt.figure(figsize=(10, 5)) 

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(122)
plt.imshow(cv2.cvtColor(inverted_image, cv2.COLOR_BGR2RGB))
plt.title('Inverted Image')
plt.axis('off')

plt.show()
