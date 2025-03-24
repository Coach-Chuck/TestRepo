import cv2
import numpy as np
# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a line
# cv2.line(image, start_point, end_point, color, thickness)
cv2.line(img, (0, 0), (511, 511), (47, 107, 85), 5)

# Draw a rectangle
# cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# Draw a circle
# cv2.circle(image, center_coordinates, radius, color, thickness)
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

text = "Hello, OpenCV!"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (255, 255, 255) # White color in BGR
thickness = 2
# Coordinates of the bottom-left corner of the text string
org = (50, 100) 
cv2.putText(img, text, org, font, font_scale, color, thickness, cv2.LINE_AA)


cv2.imshow('blank', img)
cv2.waitKey(0)
cv2.destroyAllWindows
