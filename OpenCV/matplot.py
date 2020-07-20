import matplotlib.pyplot as plt
import cv2

# 컬러 영상 출력
imgBGR = cv2.imread('OpenCV/cat.bmp')  # open cv imread 는 BGR순서 (ndarray)로 읽힌다.
# RGB로 바꾸려면 cvtColor함수를 이용해야된다
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(imgRGB)
plt.show()

# 그레이 스케일 영상 출력
imgGray = cv2.imread('OpenCV/cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)  # 121 : (1,2) size 1번째
plt.subplot(122), plt.axis('off'), plt.imshow(
    imgGray, cmap='gray')  # 122 : (1,2) size 2번째
plt.show()
