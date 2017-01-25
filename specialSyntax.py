print('aaa')
print("i'm")
print('i\'m')

print('------------')

print('aa' + str(1))
print(5 + int('5'))
print(5 + float('3.2'))

print('------------')

for i in [23, 4, 5]:
    print(i)

print('------------')

for i in range(1, 20, 2):
    print(i)

print('------------')
a, b, c = 1, 2, 3
print(a, b, c)

print('------------')

x, y, z = 2, 1, 0
if x > y > z:
    print('y more than x and y is less than z')

print('------------')

tmp = 12
# print('111aaa' + 12)  # 会报错
print('111aaa' + repr(tmp))  # 使用此方法
# print('111aaa' + `tmp`)  # 使用此方法,py3.5不支持了 ,请使用repr
print('111aaa' + str(tmp))  # 使用此方法

print('------------')

# 简单的列表推导式
abcd = [x**2 for x in range(1,4)]
print(abcd)




