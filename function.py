def aa():
    a, b = 1, 3
    print(a, b)
    print('c is ' + str(a + b))

aa()


def bb(a, b):
    print(a, b)
    print('c is', a + b)

bb(1, 2)

bb(a=1, b=2)

bb(b=2, a=1)


# 默认参数值,顺序必须在最后，思考一下觉得这规则很正常
def sale_car(price, color='red', brand='carmy', is_second=True):
    # def sale_car(price, color, brand, is_second):
    print('price:', price,
          'color:', color,
          'brand:', brand,
          'is_second:', is_second)

sale_car(1000, 'red', 'carmy', True)
sale_car(1000, color='blue')


def return_func(a):
    return a + 100

print(return_func(10))
