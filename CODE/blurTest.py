import cv2
import numpy as np
image=cv2.imread("dog.jpg")

# Define an averaging kernel (5x5)
blur_kernel = np.ones((5,5), dtype=np.float32) / 25
# Apply the kernel using filter2D
blurred = cv2.filter2D(image, -1, blur_kernel)

# Apply Gaussian Blur (built-in OpenCV function)
gaussian_blur = cv2.GaussianBlur(image, (5,5), 0)

# Apply Median Blur
median_blur = cv2.medianBlur(image, 5)

sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]], dtype=np.float32)
# Apply the sharpening kernel
sharpened = cv2.filter2D(image, -1, sharpen_kernel)

# Show the sharpened image
cv2.imshow("Sharpened Image", sharpened)

# Show the Median blurred image
cv2.imshow("Median Blur", median_blur)

# Show the Gaussian blurred image
cv2.imshow("Gaussian Blur", gaussian_blur)

# Show the blurred image
cv2.imshow("Blurred Image", blurred)

cv2.imshow('Original',image)
cv2.waitKey(0)
cv2.destroyAllWindows()