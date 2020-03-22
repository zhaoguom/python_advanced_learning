from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import time
import threading
import os

def get_html(interval):
    time.sleep(interval)
    print("sub process success")
    return interval


if __name__ == "__main__":
    process = multiprocessing.Process(target=get_html, args=(2,))
    print(process.pid)
    process.start()
    print(process.pid)
    process.join()
    print("main process end")

    print("="*20)

    # 使用进程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result = pool.apply_async(get_html, args=(3, ))
    pool.close()
    pool.join()
    print(result.get())

    print("="*20)

    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    for result in pool.imap(get_html, [1,5,3]):
        print("{} sleep success".format(result))

    print("="*20)
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    for result in pool.imap_unordered(get_html, [1,5,3]):
        print("{} sleep success".format(result))
