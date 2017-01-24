text = 'this is a new line,\n this is a new line.\nthis is a new line'

file = open('myfile.txt', 'w')
file.write(text)  # 每次都新写
file.close()

file = open('myfile-append.txt', 'a')
file.write(text)  # 每次都追加
file.close()

file = open('myfile.txt', 'r')
content = file.read()
print(content)

print('---------2---------------')

file2 = open('myfile.txt', 'r')
content2 = file2.readlines()
for i in content2:
    print(i)

print('---------e---------------')

file3 = open('myfile.txt', 'r')
content3 = file3.readline()
while content3:
    print(content3)
    content3 = file3.readline()


# rb ,wb 读取二进制文件，还可以用其它模块读取
# 其它编码的文件，比如utf-8
