import cv2

img = cv2.imread("test.jpeg")

gaussian = cv2.GaussianBlur(img, (5,5), 0)

cv2.imshow("Original", img)
cv2.imshow("Gaussian Filter", gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()