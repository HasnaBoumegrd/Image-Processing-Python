import cv2
import numpy as np

img = cv2.imread("test.jpeg", 0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

rows, cols = img.shape
crow, ccol = rows//2 , cols//2

mask = np.zeros((rows, cols), np.uint8)

mask[crow-60:crow+60, ccol-60:ccol+60] = 1
mask[crow-20:crow+20, ccol-20:ccol+20] = 0

fshift = fshift * mask

f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

cv2.imshow("Band Pass Filter", img_back / 255)

cv2.waitKey(0)
cv2.destroyAllWindows()