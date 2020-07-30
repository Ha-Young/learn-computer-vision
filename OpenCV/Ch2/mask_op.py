import numpy as np
import cv2

src = cv2.imread('OpenCV/Ch2/airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('OpenCV/Ch2/mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('OpenCV/Ch2/field.bmp', cv2.IMREAD_COLOR)

# cv2.copyTo(src, mask, dst)
# dst = cv2.copyTo(src, mask)

# mask > 0 보다 큰 (true)가 되는 행렬이 반환된다. 이 행렬을 src에 인덱싱하면 그 true가 되는 부분의 픽셀값만 가져 올 수 있다.
dst[mask > 0] = src[mask > 0]


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()

cv2.destroyAllWindows()


# png 알파채널을 가진 파일은 IMREAD_UNCHANGED로
src = cv2.imread('OpenCV/Ch2/opencv-logo-white.png', cv2.IMREAD_UNCHANGED)
mask = src[:, :, -1]  # (가로, 세로)다 가져와서 맨마지막 하나 -> 알파채널만 -> 흑백 GrayScale
src = src[:, :, 0:3]  # (가로, 세로) 다 가져와서 0,1,2 채널 (3개 채널) -> 알파채널을 뺀다는 말
dst = cv2.imread('OpenCV/Ch2/field.bmp', cv2.IMREAD_COLOR)

h, w = src.shape[:2]

# dst가 src보다 크므로 크기에 맞게 짤라주자 / 그리고 이 crop은 큰 크기의 dst와 공유한다
crop = dst[20:h + 20, 20:w+20]

# 자르는 이유는 copyTo 함수를 쓰기 위해 (src와 dst 크기가 같아야 되기 때문)
cv2.copyTo(src, mask, crop)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()
