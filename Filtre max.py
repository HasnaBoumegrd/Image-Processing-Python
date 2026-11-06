import cv2
import numpy as np

img = cv2.imread("test.jpeg", 0)

kernel = np.ones((3,3), np.uint8)

max_filter = cv2.dilate(img, kernel)

cv2.imshow("Original", img)
cv2.imshow("Max Filter", max_filter)

cv2.waitKey(0)
cv2.destroyAllWindows()