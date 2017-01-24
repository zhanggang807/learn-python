import copy

a = [1, 2, 3]
b = a          # 一样的地址
print(id(a))
print(id(b))

a[0] = 4       # a改变了，b也改变了
print(a)
print(b)

# ----------------------------------

# shadow copy
c = copy.copy(a)
print(id(a) == id(c))  # False
a[1] = 5
print(a)  # [4, 5, 3]
print(c)  # [4, 2, 3]

# ----------------------------------

# 浅复制吧
a = [1, 2, [3, 4]]
d = copy.copy(a)
print(id(a) == id(d))  # False
print( id(a[2]) == id(d[2]) )  # True
a[0] = 11
print(a)
print(d)
a[2][0] = 444
print(a)
print(d)

# ----------------------------------

# deep copy
e = copy.deepcopy(a)
print(id(e[2]) == id(a[2])) # False
