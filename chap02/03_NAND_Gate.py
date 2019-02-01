import numpy as np
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

####################


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





if __name__=="__main__":
    for xs in [(0,0),(0,1),(1,0),(1,1)]:
        y = NAND(xs[0], xs[1])
        print(str(xs) + "->"+str(y))


