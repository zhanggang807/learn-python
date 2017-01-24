char_list = ['1', '2', '3', '4']
set1 = set(char_list)
print(type(set1))
print(set1)


sentence = 'welcome to china'
print(set(sentence))  # {'t', 'l', 'h', 'i', 'm', 'w', 'e', ' ', 'c', 'a', 'o', 'n'}

set1.add('1')  # 加不上去
print(set1)
set1.add(5)     # add数字也行
print(set1)

# set1.remove('6')  # 会报错
print(set1)
set1.discard('6')
print(set1)


# 找不同

set2 = {1, 2, 3}
set3 = {2, 3, 4}
print(set2.difference(set3))  # {1}
print(set3.difference(set2))  # {4}

# 找相同
print(set2.intersection(set3)) # {2, 3}