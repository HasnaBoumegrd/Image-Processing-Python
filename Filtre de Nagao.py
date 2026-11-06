import cv2

img = cv2.imread("test.jpeg")

nagao = cv2.edgePreservingFilter(img)

cv2.imshow("Original", img)
cv2.imshow("Nagao Approximation", nagao)

cv2.waitKey(0)
cv2.destroyAllWindows()