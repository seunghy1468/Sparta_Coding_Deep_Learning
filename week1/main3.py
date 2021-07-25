import cv2

# videocapture라는 함수를 써서 동영상을 load함
# 동영상 == 이미지의 연속
cap = cv2.VideoCapture('04.mp4')

# 0을 넣으면 연결되어있는 웹 캠으로 얼굴을 띄운다
# cap = cv2.VideoCapture(0)

# 무한루프를 돌면서 순차적으로 이미지를 불러온다
# 한 frame씩 저장!
while True:
    ret, img = cap.read()

# 동영상이 끝났을 때, false가 되어 loop를 빠져나온다. 그리고 이미지를 띄운다
    if ret == False:
        break

    cv2.rectangle(img, pt1=(721, 183), pt2=(878, 465),
                  color=(255, 0, 0), thickness=2)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, dsize=(640, 360))
    # img = img[100:200, 150:250]
    cv2.imshow('result', img)

# 0을 넣어서 무한정 기다리도록 했는데,
# 1ms의 delay를 두어 이미지를 불러오도록 한다
    if cv2.waitKey(10) == ord('q'):
        break
