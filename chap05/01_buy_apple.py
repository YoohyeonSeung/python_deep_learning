from chap05._common import  *   ## 생성한 함수를 모드 쓸라면 일일이 쓸 필요 없이 *으로 쓰면됨

applePrice = 100
appleNumber = 2
tax = 1.1

Mul_apple_layer = MulLayer()
Mul_tax_layer = MulLayer()

# 순전파

apple_price = Mul_apple_layer.forward(applePrice, appleNumber)
price = Mul_tax_layer.forward(apple_price, tax)

print("사과 구입 금액 : {0}".format(int(price)))

# 역전파

dout = 1

backward_price, backward_tax = Mul_tax_layer.backward(dout)     #위의 forward함수에 의해 x1, x2가 저장되어 있다.

print("역전파 소비세 : {0}".format(backward_tax))

dapple, dapple_num = Mul_apple_layer.backward(backward_price)
print("역전파 사과 값 결과 : ", dapple)
print("역전파 사과의 갯수 : ", int(dapple_num))

