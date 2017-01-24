# 无顺序的
d = {'apple':1, 'pear': 2, 'banana':3}
d2 = {1:'a', 2:'b'}

print(d['apple'])
print(d2[1])

del d['pear']  # delete
print(d)

d['orange'] = 4  # add a element
print(d)

# dict in dict
d3 = {'dict' : {'a':8}}
print(d3)


# function as dict's value
def aa():
    print('func in dict')

d4 = {'func': aa}
print(d4)

