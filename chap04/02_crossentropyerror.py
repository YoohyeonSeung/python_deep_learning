import numpy as np

def cross_entropy_error(y, t):
    delta = 1e-7      # log(0) = - infinity이므로 그걸 보완하기 위해 아주 작은 값 delta를 더해준다
    return -np.sum(  t* np.log(y+delta))  

y=[0.1, 0.05, 0.6, 0.0, 0.05,  0.1, 0.0,  0.1, 0.0, 0.0]  # 2
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0] # One-hot Enconding

result = cross_entropy_error(np.array(y), np.array(t))
print(result)

y=[0.1, 0.05, 0.1, 0.0, 0.05,  0.1, 0.0,  0.6, 0.0, 0.0]

result = cross_entropy_error(np.array(y), np.array(t))
print(result)






