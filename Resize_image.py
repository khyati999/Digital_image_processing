import cv2
input_image_path = 'Flower.jpg'
output_image_path = 'resized_image.jpg'
new_width = 300
new_height = 200

image = cv2.imread(input_image_path)
resized_image = cv2.resize(image, (new_width, new_height))
cv2.imwrite(output_image_path, resized_image)




