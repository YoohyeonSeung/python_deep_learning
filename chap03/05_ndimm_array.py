import numpy as np

A = np.array([1,2,3,4])
print(A)
print(np.ndim(A))
print(A.shape)
print(A.shape[0])

# 2ckdnjs qoduf(행렬 / matrix)
B = np.array([[1,2],[3,4],[5,6] ])
print(B)
print(np.ndim(B))
print(B.shape)


# 행렬의 내적(행렬의 곱)
A=np.array([[1,0],[0,1]])
B=np.array([[1,2],[3,4]])

print(np.dot(A,B))


# 2x3 행렬과 3x2행렬의 내적
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[1,2],[3,4],[5,6]])
print(np.dot(A, B))

# 신경망의 내적(pdf 15p)
X=np.array([1, 2])
W = np.array([[1,3,5],[2,4,6]])
Y = np.dot(X, W)
print(Y)