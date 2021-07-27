# 1주차 숙제
# 왼쪽 위(x=721, y=183)에서 오른쪽 아래 (x=878, y=465)까지 영상 자른다
# 영상을 그레이 스케일로 변환
# 가공된 영상 출력

import cv2

video = cv2.VideoCapture(
    'C:/Users/MSI/Desktop/Work space/sparta_coding_deep_learning_clone/week1/03.mp4')

while True:
    ret, img = video.read()

# 동영상이 끝났을 때, false가 되어 loop를 빠져나온다. 그리고 이미지를 띄운다
    if ret == False:
        break

    # cropped_video = img[183:465, 721:878]
    # gray_video = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('result', img)

    if cv2.waitKey(10) == ord('q'):
        break
