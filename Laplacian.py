import cv2

img = cv2.imread("test.jpeg", 0)

lap = cv2.Laplacian(img, cv2.CV_64F)

cv2.imshow("Laplacian", lap)
cv2.waitKey(0)
cv2.destroyAllWindows()