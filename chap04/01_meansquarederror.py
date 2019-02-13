import numpy as np
## Y = W*X + b에서 W와 b를 찾는 방법이 mean squared 와 cross entropy방법이 있다. 이중 먼저 여기서는
## mean squared 방법을 먼저 해본것.
def mean_squared_error(y, t):
    return 0.5 * np.sum( np.power( y-t, 2  )   )

y=[0.1, 0.05, 0.6, 0.0, 0.05,  0.1, 0.0,  0.1, 0.0, 0.0]  # 2
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0] # One-hot Enconding

result = mean_squared_error(np.array(y), np.array(t))  # 그냥 y, t로 하면 list라서 오류가 뜸
print(result)

y=[0.1, 0.05, 0.1, 0.0, 0.05,  0.1, 0.0,  0.6, 0.0, 0.0]

result = mean_squared_error(np.array(y), np.array(t))  # 그냥 y, t로 하면 list라서 오류가 뜸
print(result)






