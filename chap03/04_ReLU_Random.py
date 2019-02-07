import numpy as np
import matplotlib.pylab as plt


def relu(x):
    return np.maximum(0, x)

if __name__=="__main__":
    print(relu(5))
    print(relu(-1))

    x = np.arange(-5.0, 5.0, 0.1) #-5.0에서 5.9까지 0.1 간격으로 값생성
    #print(x)

    y =relu(x)

    plt.plot(x, y)
    plt.ylim(-1.0, 5.5)
    plt.show()
