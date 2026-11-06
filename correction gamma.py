# ==========================================
# 1. CORRECTION GAMMA
# ==========================================

import cv2
import numpy as np

img = cv2.imread("test.jpeg", 0)

gamma = 2.0   # >1 zones claires / <1 zones sombres

gamma_corrected = np.array(255 * (img / 255) ** gamma, dtype='uint8')

cv2.imshow("Original", img)
cv2.imshow("Gamma Correction", gamma_corrected)

cv2.waitKey(0)
cv2.destroyAllWindows()