import multiprocessing as mp


def job(x):
    return x*x


def multicore():
    # pool = mp.Pool()  # 默认是全部的核
    pool = mp.Pool(processes=2)  # 使用的核的数量
    res = pool.map(job, range(10))  # 数不能太大
    print(res)

    res = pool.apply_async(job, (2,))  # 每次只给一个核？？？具体含义再研究
    print(res.get())

    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    print([res.get() for res in multi_res])

if __name__ == '__main__':
    multicore()
