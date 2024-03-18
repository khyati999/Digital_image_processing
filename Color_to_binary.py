import cv2
import matplotlib.pyplot as plt

img = cv2.imread('pikachu.jpg')
if img is None:
    print("Error: Unable to load the image.")
else:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, binary_image) = cv2.threshold(gray, 175, 255, cv2.THRESH_BINARY)

    plt.subplot(131), plt.imshow(img_rgb), plt.title('Original Image'), plt.axis('off')
    plt.subplot(132), plt.imshow(gray, cmap='gray'), plt.title('Grayscale Image'), plt.axis('off')
    plt.subplot(133), plt.imshow(binary_image, cmap='gray'), plt.title('Binary Image'), plt.axis('off')
    plt.show()