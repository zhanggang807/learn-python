import threading
import time
from queue import Queue


def job(l, q):
    for i in range(len(l)):
        l[i] **= 2
    q.put(l)


def multi_threading(data=None):
    q = Queue()
    threads = []
    data = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

    for i in range(len(data)):
        t = threading.Thread(target=job,args=(data[i], q))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    results = []
    for _ in range(3):
        results.append(q.get())

    print(results)


if __name__ == '__main__':
    multi_threading()


# python的多线程有一个Global Interpreter Lock
# 多线程如果是cpu密集型的，可能会变成线性运行，锁粒度太大了
# 多线程会请求，释放GIL，有眯鸡肋啊。不过也在改进，比较困难
# 兼顾功能和性能？如果取舍
# 建议使用multiprocessing
