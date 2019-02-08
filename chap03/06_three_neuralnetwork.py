import numpy as np


# 입력 층에서 1층으로 신호전달
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5],[0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

A1 = np.dot(X, W1) + B1

# 1층에서의 활성화 함수 처리
def sigmoid(x):
    return 1/(1+np.exp(-x))

Z1 = sigmoid(A1)

print(A1)
print(Z1)

# 1층에서 2층으로 신호전달
W2 = np.array([[0.1, 0.4],[0.2, 0.5],[0.3,0.6]])
B2 = np.array([0.1, 0.2])

A2 = np.dot(A1, W2)+B2

Z2 = sigmoid(A2)

print(A2)
print(Z2)

# 2층에서 3층으로 신호 전달
W3 = np.array([[0.1, 0.3],[0.2, 0.4]])
B3 = np.array([0.1, 0.2])



# 항등 함수의 정의 -  출력단
def identify_functdion(x):
    return x

A3 = np.dot(Z2, W3)+B3
Y = identify_functdion(A3)

print(A3)
print(Y)
