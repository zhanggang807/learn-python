# zip
a = [1, 2, 3]
b = [4, 5, 6]
# 竖向合并，跟迪卡尔积不一样
ab = zip(a, b)
print(ab)        # <zip object at 0x00000000021BA088>
print(list(ab))  # [(1, 4), (2, 5), (3, 6)]

# simple function
def func1(x, y):
    return x +y

print(func1(1, 2))

# lambda , better than simple function
func2 = lambda x, y: x + y

print(func2(1, 2))

# map 映射，很好用啊
result = map(func1, [1], [2])
print(result)           # <map object at 0x0000000002206BA8>
print(list(result))     # [3]

result1 = map(func1, [1, 3], [2, 5])
print(result1)           # <map object at 0x0000000002666C88>
print(list(result1))     # [3, 8]