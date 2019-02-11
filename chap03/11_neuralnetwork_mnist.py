import sys, os
sys.path.append(os.pardir) # 부모 디렉토리의 파일을 가져올 수 있도록 설정.
import numpy as np
from dataset.mnist import load_mnist
import pickle

def sigmoid(x):
    y = 1 / (1 + np.exp(-x))
    return y

def softmax(a):
    c=np.max(a)
    exp_a = np.exp(a-c)    # 오버플로 처리
    sum_exp_a = np.sum(exp_a)
    return exp_a/sum_exp_a



def get_data():
    (x_train, t_train,), (x_test, t_test) = load_mnist(flatten=True, normalize=True, one_hot_label=False)
    # 0~1까지 정규화, 3차원데이터를 1차원으로 변경
    return x_test, t_test
    #반환형은 튜플!

def init_network():
    with open("sample_weight.pkl", 'rb') as f :
        network = pickle.load(f)

    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)

    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)

    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y

if __name__ == "__main__":
    x, t = get_data()
    network = init_network()

    accuracy_cnt = 0

    for i in range(len(x)):
        y = predict(network, x[i])
        p = np.argmax(y)
        if p==t[i]:
            accuracy_cnt+=1
    print("Accuracy : "+ str(float(accuracy_cnt)/len(x)) )



























