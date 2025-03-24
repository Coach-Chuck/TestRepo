import cv2
import numpy as np
image=cv2.imread("Turtle.jpeg")
gray_image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rgb_image= cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hsv_image= cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hls_image= cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
yuv_image= cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
lab_image= cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

cv2.imshow('RGB', rgb_image)
cv2.imshow('Gray', gray_image)
cv2.imshow('Original', image)
cv2.waitKey(0)
cv2.destroyAllWindows