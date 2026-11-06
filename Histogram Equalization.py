import cv2

img = cv2.imread("test.jpeg", 0)

eq = cv2.equalizeHist(img)

cv2.imshow("Equalized", eq)
cv2.waitKey(0)
cv2.destroyAllWindows()