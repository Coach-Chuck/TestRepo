import cv2

img = cv2.imread("cat.jpg")
img2 = cv2.imread("dog.jpg")
img3 = cv2.imread("echidna.jpg")
img4 = cv2.imread("giraffe.jpg")
resized_img = cv2.resize(img,None, fx=0.3, fy=0.3,interpolation=cv2.INTER_AREA)

cv2.imshow("Cat(Resized)",resized_img)
cv2.imshow("Dog",img2)
cv2.imshow("Echidna",img3)
cv2.imshow("Giraffe",img4)
cv2.imshow("Cat BIg Pic",img)
cv2.waitKey(0)
