from multiprocessing import Process, Queue
import time

# 共享全局变量不能适用于多进程通信


def producer(a):
    a += 1
    time.sleep(2)


def consumer(a):
    time.sleep(2)
    print(a)


if __name__ == "__main__":
    a = 1
    my_procuder = Process(target=producer, args=(a,))
    my_consumer = Process(target=consumer, args=(a,))
    my_procuder.start()
    my_consumer.start()
    my_procuder.join()
    my_consumer.join()
