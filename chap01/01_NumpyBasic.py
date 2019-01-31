# 배열 or 행렬 계산 - NumPy(Numerical Python : 과학적 계산(선형대수))
import numpy as np

# 1. 배열 생성
x = np.array([10, 20, 30])
print(x)

print(type(x)) #<class 'numpy.ndarray'>
print(x.shape) # (3,)
print(x[0], x[1], x[2])  # 10 20 30

y=np.array([[1,2,3],[4,5,6]])
print(y)
# z=np.array([1,2,3],[4,5,6]) # TypeError: data type not understood

print(y.shape)
print(y[0,1])   # 2
print(y[0][1])  # 위의 코드와 같이 써도 무방


# 2. 산술 연산
x = np.array([1., 2., 3.])
y = np.array([4., 5., 6.])
print(x+y)
print(x-y)
print(x*y)
print(x/y)

x = np.array([1., 2., 3.])
print(x/2.0) #[0.5 1.  1.5]

# 3. N차원 배열
A = np.array([     [1,2] , [3,4]    ])
print(A)
print(A.shape)
print(A.dtype)

B = np.array([     [3,0] , [0,6]    ])
print(B)
print(B.shape)
print(B.dtype)

print(A+B)
print(A*B)
#print(A/B)




'''
C= np.array( [ [ [1,2 ],[3,4 ] ], [  [5,6] , [7,8]  ]     ])
print(C)
print(C.shape)
print(C.dtype)
'''


# 4. 브로드캐스트
X=np.array([  [1,2],      [3,4]  ])
Y=np.array([10, 20])
print(X*Y)


'''
# cf)
Y=np.array([10, 20, 30])

print(X*Y) #계산은 안됨

'''


# 5. 원소 접근(index)
X=np.array([[5, 6],[20, 21],[9,1] ])
print(type(X))
print(X[0])
print(X[0][1])


print(X.flatten()) #1행으로 평평하게 펼쳐라
X=X.flatten()
print(X[np.array([0,2,4])])

print(X>15)









































