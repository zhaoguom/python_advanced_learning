from multiprocessing import Process, Queue, Pool, Manager
import time

# multiprocessing中的Queue不能用于Pool进程池， 用Manager来完成这中需求

# from queue import Queue  -- 线程间通信
# from multiprocessing import Queue   -- 进程间通信
# from multiprocessing import Manager (实例化之后在里面有个Queue)   -- 进程池中的进程间通信


def producer(queue):
    queue.put("a")
    time.sleep(2)

def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)

if __name__ == "__main__":
    queue = Manager().Queue(10)
    pool = Pool(2)

    pool.apply_async(producer, args=(queue, ))
    pool.apply_async(consumer, args=(queue, ))
    pool.close()
    pool.join()
