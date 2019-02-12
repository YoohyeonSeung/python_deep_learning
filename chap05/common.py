class MulLayer:
    def __init__(self):
        self.x1=None
        self.x2=None

    def forward(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
        out = x1 * x2
        return out

    def backward(self, dout):
        dx1 = dout * self.x2
        dx2 = dout * self.x1
        return dx1, dx2

class AddLayer:
    def __init__(self):
        self.x1 = None
        self.x2 = None

    def forward(self, x1, x2):
        out = x1 + x2
        return out

    def backward(self, dout):
        dx1 = dout * 1
        dx2 = dout * 1

        return dx1, dx2