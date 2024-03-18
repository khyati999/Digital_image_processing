import cv2
import numpy as np
input_image_path = 'Flower.jpg'
output_image_path = 'brightness_and_contrast.jpg'
alpha = 1.5  
beta = 50   

image = cv2.imread(input_image_path)
adjusted_image = cv2.addWeighted(image, alpha, np.zeros_like(image), 0, beta)
cv2.imwrite(output_image_path, adjusted_image)