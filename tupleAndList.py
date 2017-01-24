# tuple tuple的api好像比较少啊

a_tuple = (1, 2, 3, 4, 5)
another_tuple = 1, 2, 3, 4, 5
for i in a_tuple:
    print(i)

print('-------------')

# list
a_list = [1, 2, 3, 4, 5, 6, 7]

for i in a_list:
    print(i)


for index in range(len(a_list)):
    print('index;', index, 'number:', a_list[index])


# todo 元组，列表，切片，追加，扩展，弹出等应用

a = [1, 2, 3]
a.append(0)
print(a)

b = [4, 5]
a.extend(b)
print(a)

a.insert(0, 9)
print(a)

a.remove(9)  # remove value
# a.remove(a[2])  # remove index
print(a)

print(a.count(1))

print(a[-1])
print(a[3:5])
print(a[3:4])
print(a)

print(a.count(3))  # 值出现的数量

print(a.index(2)) # 值的索引

a.reverse()
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
