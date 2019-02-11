import sys, os
sys.path.append(os.pardir)
import numpy as np
import pickle
from dataset.mnist import load_mnist

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


    batch_size = 100 # 배치크기
    accuracy_cnt = 0

    for i in range(len(x), batch_size):
        x_batch = x[i:i+batch_size]
        y_batch = predict(network, x_batch)
        p = np.argmax(y_batch, axis=1)  # axis는 차원을 의미 1차원
        accuracy_cnt += np.sum(p == t[i:i + batch_size])

    print('Accuracy : ' + str(round(float(accuracy_cnt) / len(x) * 100, 2)) + "%")