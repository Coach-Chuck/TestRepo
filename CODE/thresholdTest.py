import cv2 
# Load the image in grayscale (no color, just black & white) 
image = cv2.imread("Turtle.jpeg", cv2.IMREAD_GRAYSCALE) 
# Pick a threshold value, let's say 127 
threshold_value = 127 
# Convert the image based on that threshold value
_, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY) 
 
# Apply adaptive thresholding (it decides the best threshold for each part) 
adaptive_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2) 
# Show the new image
cv2.imshow("Adaptive Thresholding", adaptive_image)

# Show the new image 
cv2.imshow("Binary Image", binary_image) 

cv2.imshow('Gray', image)

cv2.waitKey(0)
cv2.destroyAllWindows()