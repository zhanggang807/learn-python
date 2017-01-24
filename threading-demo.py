import threading
import time


def thread_job():
    print("t1 start,this is a adding thread, number is %s" % threading.current_thread())
    for i in range(30):
        time.sleep(0.1)

    print('t1 finish')


def t2_job():
    print('t2 start')
    print('t2 end')


def main():
    added_tread = threading.Thread(target=thread_job, name='t1')
    added_tread.start()

    added_tread2 = threading.Thread(target=t2_job, name='t2')
    added_tread2.start()

    # added_tread.join()  #在主线程里join的
    # added_tread2.join()  #在主线程里join的

    print('all done')

    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())
    # print(threading.current_thread().name)


if __name__ == '__main__':
    main()
