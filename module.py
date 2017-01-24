
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
