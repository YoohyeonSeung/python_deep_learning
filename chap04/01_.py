import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum( np.power( y-t, 2  )   )

y=[0.1, 0.05, 0.6, 0.0, 0.05,  0.1, 0.0,  0.1, 0.0, 0.0]  # 2
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0] # One-hot Enconding

result = mean_squared_error(np.array(y), np.array(t))  # 그냥 y, t로 하면 list라서 오류가 뜸
print(result)

y=[0.1, 0.05, 0.1, 0.0, 0.05,  0.1, 0.0,  0.6, 0.0, 0.0]

result = mean_squared_error(np.array(y), np.array(t))  # 그냥 y, t로 하면 list라서 오류가 뜸
print(result)






