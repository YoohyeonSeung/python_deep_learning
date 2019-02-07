import numpy as np
import matplotlib.pylab as plt
import antigravity

def sigmoid(x):
    return 1/(1+np.exp(-x))

if __name__=="__main__":
    x = np.arange(-5.0, 5.0, 0.1) #-5.0에서 5.9까지 0.1 간격으로 값생성
    #print(x)

    y = sigmoid(x)

    print(y)

    plt.plot(x, y)
    plt.show() #최종적으로 그래프 보는 명령어 코드