import cv2
import numpy as np

# Create a blank image (you can also load an existing image with cv2.imread())
img = np.zeros((512, 512, 3), np.uint8)  # 512x512, 3 channels (BGR), 8-bit unsigned int

# Line: cv2.line(image, start_point, end_point, color, thickness)
cv2.line(img, (0, 0), (511, 511), (0, 255, 0), 5)  # Green line, thickness 5

# Rectangle: cv2.rectangle(image, top_left, bottom_right, color, thickness)
cv2.rectangle(img, (100, 100), (300, 200), (255, 0, 0), 3)  # Blue rectangle, thickness 3

# Circle: cv2.circle(image, center_coordinates, radius, color, thickness)
cv2.circle(img, (256, 256), 50, (0, 0, 255), -1)  # Red filled circle (-1 for filled)

# Ellipse: cv2.ellipse(image, center_coordinates, axes, angle, start_angle, end_angle, color, thickness)
cv2.ellipse(img, (256, 150), (100, 50), 0, 0, 360, (255, 255, 0), 2) # Cyan Ellipse

# Polygon: cv2.polylines(image, [points], isClosed, color, thickness)
pts = np.array([[10, 50], [150, 80], [250, 200], [50, 250]], np.int32)
pts = pts.reshape((-1, 1, 2)) # Reshape for polylines
cv2.polylines(img, [pts], True, (0, 255, 255), 3) # Yellow Polygon

# Display the image
cv2.imshow('Shapes', img)
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()

# import cv2
# import numpy as np

# img = cv2.imread("dog.jpg")

# # Text: cv2.putText(image, text, bottom_left_corner, font, font_scale, color, thickness, lineType)
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img, 'Hello OpenCV', (10, 30), font, 1, (0, 0, 0), 2, cv2.LINE_AA)  # Black text

# cv2.imshow('Text', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()