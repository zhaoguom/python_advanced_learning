# 获取锁和释放锁需要时间，会影响性能，使用不当会引起死锁
# RLock, 在同一个线程里可以连续调用多次acquire，一定要注意acquire的次数要和release的次数相同

import threading
from threading import Lock, RLock

total = 0
lock = RLock()

def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        lock.acquire()
        total +=1
        lock.release()
        lock.release()

def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -=1
        lock.release()

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(total)