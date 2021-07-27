# 내 사진을 고흐 화풍으로!
import cv2
import numpy as np

# print(cv2.__version__)
# 다운받은 img load
# opencv의 dnn 모델을 사용하는데, torch로부터 net을 읽는다
# torch: deep learning framwork 중 하나
net = cv2.dnn.readNetFromTorch(
    'C:/Users/MSI/Desktop/Work space/sparta_coding_deep_learning_clone/week2/models/instance_norm/mosaic.t7')

img = cv2.imread(
    'C:/Users/MSI/Desktop/Work space/sparta_coding_deep_learning_clone/week2/imgs/02.jpg')

# img 전처리 (processing)
# 성능 향상(얼마나 정답을 잘 맞추는지, 정확도 향상)을 위함
# 이미지의 형태. h, w, c라는 변수에 넣어준다
h, w, c = img.shape

# 이미지 비율 유지하면서 크기 변겅 (비례식 이용)
# h : w = new_h : 500
# 소수점이 나올 수 있기 때문에, int로 묶어준다
img = cv2.resize(img, dsize=(500, int(h / w * 500)))

# ------------- img 자르는 code -----------
img = img[162:513, 185:428]

print(img.shape)

# ---------------전처리 (pre processing) -----------
# img를 전처리한다. MEAM_VALUE를 넣어줘야 굉장히 편하다
# blobfromeimage: 차원변형을 해준다.
MEAN_VALUE = [103.939, 116.779, 123.680]
blob = cv2.dnn.blobFromImage(img, mean=MEAN_VALUE)

# 차원변형을 해서 컴퓨터가 이해할 수 있는 형태로 바꿔준다
# 순서가 바뀜 (img.shape와 비교!)
print(blob.shape)

# blob을 인풋으로 넣어라
net.setInput(blob)

# -------------- 결과 추론하기 (inference) -------------
# 우리가 봤을 때, 이해하도록 바꿔주어야 한다 (후처리, post processing)
output = net.forward()

# 아까 차원을 늘렸는데, squeeze로 차원을 줄이고, transpose차원을 거꾸로 한다
# 그리고 MEAN_VALUE를 뻇었으니, 더해준다
output = output.squeeze().transpose((1, 2, 0))
output += MEAN_VALUE

# 가끔씩 MEAN_VALUE가 255를 초과할 경우가 있는데, 이를 제한한다.
# 이후 정수형태로 바꿔주는 unit8로 바꾼다. (사람이 볼 수 있는 img 형태)
output = np.clip(output, 0, 255)
output = output.astype('uint8')

cv2.imshow('img', img)
cv2.imshow('output', output)
cv2.waitKey(0)
