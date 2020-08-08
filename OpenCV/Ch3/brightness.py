import sys
import numpy as np
import cv2

# src = cv2.imread('OpenCV/Ch3/lenna.bmp', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('OpenCV/Ch3/lenna.bmp', cv2.IMREAD_COLOR)

# dst = cv2.add(src, 100)
# dst = np.clip(src + 100., 0, 255).astype(np.uint8)
dst = cv2.add(src, (100, 100, 100, 0))


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
