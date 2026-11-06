import cv2

img = cv2.imread("test.jpeg")

median = cv2.medianBlur(img, 5)

cv2.imshow("Median", median)
cv2.waitKey(0)
cv2.destroyAllWindows()