# 继承都没有讲，多继承
# 还有一些super , __init__这样的方法,，自省，成员访问等

# class Calculator(Frame):
class Calculator:
    name = 'calculator'
    price = 18
    # 成员变量吧

    def add(self, x, y):
        print(self.name)
        # print(name)  # 在类里要用self.name才行
        result = x + y
        print(result)

    # def xxx(self, x, y):
    #     xxx

    # def yyy(self, x, y):
    #     yyy

    def __init__(self, name, price, height, width=100):
        # self.name = name
        # self.price = price
        self.height = height
        self.width = width
        self.add(1, 2)  # 调用类内的函数

# todo 其它的__xxx__()方法呢?

# cal = Calculator()  # 无参的就不能用了
# print(cal.name)
# print(cal.price)
# cal.add(10, 11)
# cal.add(x=10, y=11)


cal1 = Calculator('name', 190, 200, 300)
print(cal1.name)
print(cal1.price)
cal1.add(10, 11)
cal1.add(x=10, y=11)
print('------')
cal2 = Calculator('name', 190, 200)
print(cal2.name)
print(cal2.price)
cal2.add(10, 11)
cal2.add(x=10, y=11)
