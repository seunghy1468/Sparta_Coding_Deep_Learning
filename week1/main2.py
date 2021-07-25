# image overlay
# 이미지를 덮어 띄우기
# overlay는 png파일이어야하고, 투명배경이어야함

import cv2

# png 파일을 불러서 overlay를 입힐 땐, unchanged를 쓴다
img = cv2.imread('01.jpg')
overlay_img = cv2.imread('dices.png', cv2.IMREAD_UNCHANGED)

overlay_img = cv2.resize(overlay_img, (150, 150))

# A채널 추가
# BGRA 총 4개의 채널! (A == 투명도 표현, 0일때 투명)
# numpy의 어레이 슬라이싱(채널부분을 잘라야함)에 대한 개념을 알고있으면 좋다
# ex) 주사위 기준으로 주사위만 제외하고 다 0, 배경을 기준으로 주사위 부분만 0

# 높이 너비 채널(4번째부터 시작해야하므로 3: 으로 표현한다(B=0, G=1, R=2, A=3))
# 0부터 1의 값으로 표현해주기 위해서 255로 나눈다
overlay_alpha = overlay_img[:, :, 3:] / 255.0
background_alpha = 1.0 - overlay_alpha

# 우리가 합성을 하고자 하는 위치 : x1, y1 = 100, 100, x2, y2 = 250, 250
# 150의 의미는 150x150으로 resize한 크기와 같아야 한다
x1 = 100
y1 = 100
x2 = x1 + 150
y2 = y1 + 150

# 주사위의 투명도 값(overlay_alpha)을 곱하면, 주사위가 있는 부분만 투명하게 됨
# :3, 3까지만 잘라라! 그래야 RGB까지(2번까지)만 나오기 때문에..
# background_img에선 img를 슬라이싱할 필요가 없다. 원래 3채널 이미지이기 떄문!
# overlay img는 4채널!
img[y1:y2, x1:x2] = overlay_alpha * overlay_img[:,
                                                :, :3] + background_alpha * img[y1:y2, x1:x2]

cv2.imshow('img', img)
cv2.waitKey(0)
