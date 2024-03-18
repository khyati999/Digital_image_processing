import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Flower.jpg',cv.IMREAD_GRAYSCALE)

plt.figure()

hist = cv.calcHist([img], [0], None, [256], [0,256])
plt.subplot(223),plt.plot(hist)
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.title('Histogram')


equ = cv.equalizeHist(img)


hist = cv.calcHist([equ], [0], None, [256], [0,256])
plt.subplot(224),plt.plot(hist)
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.title('Histogram(Equalized)')


plt.subplot(221),plt.imshow(cv.cvtColor(img,cv.COLOR_BGR2RGB))
plt.title('Original Image')
plt.subplot(222),plt.imshow(cv.cvtColor(equ,cv.COLOR_BGR2RGB))
plt.title('Equalized Image')
plt.show()
