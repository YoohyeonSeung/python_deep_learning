import numpy as np
import matplotlib.pylab as plt

def step_funtion(x):
    y=x>0
    return y.astype(np.int)

if __name__=="__main__":
    x = np.arange(-5.0, 5.0, 0.1) #-5.0에서 5.9까지 0.1 간격으로 값생성
    #print(x)

    y = step_funtion(x)

    print(y)

    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show() #최종적으로 그래프 보는 명령어 코드