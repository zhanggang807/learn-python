
APPLE = 100  # global variable

a = None


def fun():
    global a
    # 函数内声明全局变量，需要在外面先声明变量
    # 外面就可以引用这个改变过值的全局变量
    print(a)
    a = 20
    print(a)
    # a = 10
    a = APPLE
    print(a)

fun()


def fun1():
    a = 10
    return a + 10

print(fun1())

print(APPLE)
print(a)  # local variable
