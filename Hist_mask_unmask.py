import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("pikachu.jpg",0)
image=cv2.imread("pikachu.jpg")
hist=cv2.calcHist([img],[0],None,[256],[0,256])
histR=cv2.calcHist([image],[0],None,[256],[0,256])
histG=cv2.calcHist([image],[1],None,[256],[0,256])
histB=cv2.calcHist([image],[2],None,[256],[0,256])
mask=np.zeros(img.shape[:2],np.uint8)
mask[100:300,100:400]=255

masked_img=cv2.bitwise_and(img,img,mask=mask)
hist_mask=cv2.calcHist([img],[0],mask,[256],[0,256])
plt.subplot(231),plt.imshow(img,cmap='gray'),plt.title("")
plt.subplot(232),plt.imshow(mask,cmap='gray')
plt.subplot(233),plt.imshow(masked_img,cmap='gray')
plt.subplot(234),plt.plot(hist)
plt.show()

plt.title("Histogram of all RGB Colors") 
plt.plot(histR,color="Red")
plt.plot(histG,color="Green")
plt.plot(histB,color="Blue")
plt.show()