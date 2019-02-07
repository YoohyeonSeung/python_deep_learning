import numpy as np
# from 02_AND_bias import AND

# AND gate
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7 # 사람이 매개변수 값을 정함

    tmp = w1 * x1 + w2 * x2

    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

# NAND gate
def NAND(x1, x2):
    x=np.array([x1, x2])

    w=np.array([-0.5, -0.5])

    bias = 0.7

    tmp = np.sum(x*w)+bias

    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

# OR gate
def OR(x1, x2):
    x=np.array([x1, x2])            # AND와는 모드 같은 구조의 피셉트론

    w=np.array([0.5, 0.5])

    bias = -0.2

    tmp = np.sum(x*w)+bias

    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

# XOR gate
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)

    y = AND(s1, s2)
    return y




if __name__=="__main__":
    for xs in [(0,0),(0,1),(1,0),(1,1)]:
        y = XOR(xs[0], xs[1])
        print(str(xs) + "->"+str(y))


