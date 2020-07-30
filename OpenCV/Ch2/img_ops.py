import numpy as np
import cv2

img1 = np.empty((240, 320), dtype=np.uint8)
img2 = np.zeros((240, 320, 3), dtype=np.uint8)
img3 = np.ones((240, 320, 3), dtype=np.uint8) * 255
img4 = np.full((240, 320), 128, dtype=np.uint8)
img5 = np.full((240, 320, 3), (0, 255, 255), dtype=np.uint8)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.imshow('img5', img5)

cv2.waitKey()

# 새 영상 생성하기
img1 = cv2.imread('OpenCV/Ch2/HappyFish.jpg')

img2 = img1  # img2는 img1 참조
img3 = img1.copy()  # img3는 img1 참조가 아닌 값 복사하여 새로운 img생성한 것

img1[:, :] = (255, 255, 0)  # 하늘색으로 모두 채우기

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)


cv2.waitKey()

img1 = cv2.imread('OpenCV/Ch2/HappyFish.jpg')
img2 = img1[40:120, 30:150]
img3 = img1[40:120, 30:150].copy()


img1[:, :] = (125, 255, 0)

img2.fill(0)
cv2.circle(img2, (50, 50), 20, (0, 0, 255), 2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

cv2.waitKey()
