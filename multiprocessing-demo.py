import multiprocessing as mp
# import threading as td


def job(queue, a, b):
    res =0
    for i in range(1000):
        res += i + i**2 + i**3
    queue.put(res)


# 里面有队列，多进程的 Queue
if __name__ == '__main__':
    # t1 = td.Thread(target=job, args=(1, 2))
    queue = mp.Queue()
    p1 = mp.Process(target=job, args=(queue, 1, 2)) # args如果是一个参数的话要加，
    p2 = mp.Process(target=job, args=(queue, 1, 2))
    # t1.start()
    p1.start()
    p2.start()
    print('main done')
    res1 = queue.get()
    res2 = queue.get()

    print(res1 + res2)
