import multiprocessing as mp
import time


def job(v, num, l):
    for i in range(1000):  # 1000次才会有两核交替输出
        # time.sleep(0.1)
        l.acquire()
        v.value += num  # 会有并发问题
        l.release()
        pro_name = mp.current_process().name
        print(pro_name + '==' + str(v.value))  # 怎么打印当前核呢？


def multicore():
    lock = mp.Lock()
    v = mp.Value('i', 0)
    p1 = mp.Process(target=job, args=(v, 1, lock))
    p2 = mp.Process(target=job, args=(v, 3, lock))
    p1.start()
    p2.start()


if __name__ == '__main__':
    multicore()
