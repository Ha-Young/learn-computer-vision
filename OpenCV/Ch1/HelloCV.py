import cv2
import sys

image = cv2.imread('OpenCV/cat.bmp', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("cat't read image")
    sys.exit()


window = cv2.namedWindow('cat', cv2.WINDOW_NORMAL)
cv2.imshow('cat', image)

while True:
    if cv2.waitKey() == ord('q'):
        break

cv2.imwrite('cat_gray.png', image)

cv2.destroyAllWindows()
