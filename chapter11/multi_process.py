import multiprocessing

# 耗cpu的操作，多进程可以利用多核cpu (计算类)
# io操作而言，多线程更高效

def fib(n):
    if n<=2:
        return 1
    return fib(n-1) + fib(n-2)

def random_sleep(n):
    time.sleep(n)
    return n

# from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor, as_completed
import time

if __name__ == "__main__":
    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2]*30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {}".format(data))
        print("elapsed time: {}".format(time.time()-start_time))
