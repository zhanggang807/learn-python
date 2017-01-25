import  multiprocessing as mp

var = mp.Value('d', 1)  # 核之间的数据共享

array = mp.Array('i', [1, 2, 3])  # 只能是一维的
