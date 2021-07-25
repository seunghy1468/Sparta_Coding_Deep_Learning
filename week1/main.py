import cv2
import tensorflow as tf
import dlib

# print(cv2.__version__)
# print(dlib.__version__)
# print(tf.__version__)

img = cv2.imread('01.jpg')

# 각 pixel은 BGR 정보를 포함하고있다
# 컴퓨터는 이미지를 숫자로 인식한다
# 영상 띄우기
print(img)
print(img.shape)
# 404: 이미지의 높이 (pixel), 640: 이미지의 너비 (pixel), 3: 이미지의 채널 (RGB)

# img에 사각형을 그릴것이다
# pt1= 사각형의 왼쪽 위 좌표(x,y), pt2= 사각형의 오른쪽 위 좌표
cv2.rectangle(img, pt1=(259, 89), pt2=(380, 348),
              color=(255, 0, 0), thickness=2)

# center = 원의 중심, radius = 반지름
cv2.circle(img, center=(320, 220), radius=100, color=(0, 0, 255), thickness=3)


# ------------ img 만져보기 --------------
# img 자르기 (y축, x축 순서로 img를 자른다)
cropped_img = img[89:348, 259:380]

# img 크기 변경 (deep learning 에서 resize해서 넣는 경우가 많다)
# 꼭 알아두어야 함
resized_img = cv2.resize(img, (512, 256))

# ----------- img color system --------------
# 주로 사용하는 방법 BGR
# CMYK라는 방식도 있음
# cvt == convert
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.waitKey(0)

# img 라는 window에다가 띄우겠다
cv2.imshow('gray', img_gray)
cv2.imshow('result', img_rgb)
cv2.imshow('resized_img', resized_img)
cv2.imshow('cropped img', cropped_img)
cv2.imshow('img', img)
cv2.waitKey(0)
