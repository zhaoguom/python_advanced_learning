#  gil = global interpreter lock
#  gil使得同一时间只有一个线程在一个cpu上执行字节码，
#  无法将多个线程映射到多个cpu上
#  gil 在遇到io操作的时候主动释放，这样使得python 的多线程适用于io较多的操作

import threading

total = 0

def add():
    global total
    for i in range(1000000):
        total +=1

def desc():
    global total
    for i in range(1000000):
        total -=1

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(total)