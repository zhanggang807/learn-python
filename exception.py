
try:
    file = open('eee.txt', 'r+')
except Exception as e:
    print('there is no file named as eee.txt')
    response = input('do you want to create a new file')
    if response == 'y':
        file = open('eee.txt', 'rw')
    else:
        pass
else:
    file.write('ssss')
    print('wirte success')

file.close()

# 这个例子好像有问题，先了解语法吧