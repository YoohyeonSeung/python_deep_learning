import numpy as np
# 4차원 데이터 생성 1채널에 28by28, 한번처리시마다 10개의 data 각원소는 무작위
#  즉, 4차원에서 3차원짜리가 10개 생성된것
x = np.random.rand(10, 1, 28, 28)
print(x.shape)

print(x[0].shape)  # (1, 28, 28)
for i in range(10):
    print(x[i].shape)

print(x[0][0].shape)  # 28 by 28 matrix

print(x[0, 0])      # print(x[0][0])과 같은 접근 방법