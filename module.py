
# 导入模块 起别名

import time as t

print(t.localtime())
print(t.clock())
print(t.daylight)
print(t.time())

# 好像静态导入
# from time import *

from time import time, localtime

print(localtime())

# 包的概念，还有模块放置的位置

# import xx.yy xx是包yy是yy.py

dir(time)  # 查看模块中都有什么
