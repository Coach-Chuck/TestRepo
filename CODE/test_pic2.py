import cv2

image = cv2.imread('Sushi.jpg')

width=1000
height=500

resized_image=cv2.resize(image,(width,height),interpolation=cv2.INTER_AREA)
cv2.imwrite('Sushi2.jpg', resized_image)
