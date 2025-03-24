import cv2

def convert_color_space(image, desired_color_space):
  """
  Converts an image to the specified color space.

  Args:
    image: The input image in BGR format.
    desired_color_space: 
      - 'GRAY': Grayscale
      - 'HSV': HSV color space
      - 'HLS': HLS color space
      - 'YUV': YUV color space
      - 'LAB': LAB color space
      - 'RGB': RGB color space

  Returns:
    The image converted to the desired color space.
  """

  if desired_color_space == 'GRAY':
    converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  elif desired_color_space == 'HSV':
    converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  elif desired_color_space == 'HLS':
    converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
  elif desired_color_space == 'YUV':
    converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
  elif desired_color_space == 'LAB':
    converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
  elif desired_color_space == 'RGB':
    converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  else:
    raise ValueError(f"Invalid color space: {desired_color_space}")

  return converted_image

# Example usage:
image_path = 'dog.jpg' 
image = cv2.imread(image_path)

# Convert to Grayscale
gray_image = convert_color_space(image, 'GRAY')

# Convert to HSV
hsv_image = convert_color_space(image, 'HSV')

# Convert to RGB
rgb_image = convert_color_space(image, 'RGB')

# Display the images (optional)
cv2.imshow('Original', image)
cv2.imshow('Grayscale', gray_image)
cv2.imshow('HSV', hsv_image)
cv2.imshow('RGB', rgb_image )
cv2.waitKey(0)
cv2.destroyAllWindows()