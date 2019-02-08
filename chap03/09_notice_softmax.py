import numpy as np

#def softmax(a):
#    exp_a = np.exp(a)
#    sum_exp_a = np.sum(exp_a)
#    return exp_a/sum_exp_a


#a = np.array([1010, 1000, 990])
#y = softmax(a)
#print(y)

## 오버플로우로 인하여 nan이 나옴 아래의 방법으로 그것을 커버

a = np.array([1010, 1000, 990])

max = np.max(a)
result = np.exp(a-max)/np.sum(np.exp(a-max)) ##pdf 24p, C'이 max
print(result)

def softmax(a):
    c=np.max(a)
    exp_a = np.exp(a-c)    # 오버플로 처리
    sum_exp_a = np.sum(exp_a-c)
    return exp_a/sum_exp_a

a = np.array([1010, 1000, 990])
y = softmax(a)
print(y)


x= np.array([0.3, 2.9, 4.0])
y=softmax(x)
print(y)
print(np.sum(y))