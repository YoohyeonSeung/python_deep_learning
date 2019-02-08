import sys, os
sys.path.append(os.pardir) # 부모 디렉토리의 파일을 가져올 수 있도록 설정.
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image
# pip install pillow 또는 pip install image를 해줄것

def img_show(img):
    pil_image = Image.fromarray(np.uint8(img))
    pil_image.show()



(x_train, t_train, ),(x_test, t_test)=load_mnist(flatten=True, normalize=False, one_hot_label=False)

img = x_train[2]
label = t_train[2]
print(label)
print(img.shape)
img = img.reshape(28, 28)  # 형상을 원래 이미지의 크기로 변형.
print(img.shape)

img_show(img)