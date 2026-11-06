import cv2
import numpy as np

img = cv2.imread("test.jpeg", 0)

kernelx = np.array([[1,1,1],
                    [0,0,0],
                    [-1,-1,-1]])

kernely = np.array([[-1,0,1],
                    [-1,0,1],
                    [-1,0,1]])

x = cv2.filter2D(img, -1, kernelx)
y = cv2.filter2D(img, -1, kernely)

prewitt = cv2.addWeighted(x, 0.5, y, 0.5, 0)

cv2.imshow("Prewitt", prewitt)

cv2.waitKey(0)
cv2.destroyAllWindows()