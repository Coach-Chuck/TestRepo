import cv2
image = cv2.imread('Sushi.jpg')
if image is None:
    print("Error: Image not loaded")
else:
    cv2.imshow('Sushi', image)
cv2.waitKey(10000)
cv2.destroyAllWindows()