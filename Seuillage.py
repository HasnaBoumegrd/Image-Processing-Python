import cv2

img = cv2.imread("test.jpeg", 0)

_, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Threshold", th)
cv2.waitKey(0)
cv2.destroyAllWindows()