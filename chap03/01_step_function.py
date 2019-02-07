import numpy as np


def step_function(x):
    if x > 0:
        return 1
    else:
        return 0


def step_function_nparray(x):
    y = x > 0
    return y.astype(np.int)


if __name__ == '__main__':
    x = step_function(3.0)
    print(x)

    y = step_function(-3.0)
    print(y)

    z = np.array([-1.0, 1.0, 2.0])
    step_function_nparray()

"""
    # z = np.array([-1.0, 1.0, 2.0]) # error
    # print(step_function(z))

    z = np.array([-1.0, 1.0, 2.0])
    print(z)

    y = z > 0
    print(y)

    y = y.astype(np.int)
    print(y)

"""