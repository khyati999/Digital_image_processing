import cv2
import numpy as np

image_path = 'Flower.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

mean_value = np.mean(image)
std_deviation = np.std(image)

print(f"Mean: {mean_value}")
print(f"Standard Deviation: {std_deviation}")