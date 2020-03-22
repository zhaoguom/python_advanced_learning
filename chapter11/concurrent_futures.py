from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
import time
# ThreadPool
# 主线程中可以获取某一个线程的状态或者返回值
# 当一个线程完成的时候，主线程能立即知道
# futures 可以让多线程和多进程编码接口一致


def get_html(times):
    time.sleep(times)
    print("got page {} success".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)


# 通过submit函数提交执行的函数到线程池中，submit是立即返回
task1 = executor.submit(get_html, (3))
task2 = executor.submit(get_html, (2))

# done方法用于判定某个任务是否完成
print(task1.done())

# cancel 可以取消已经提交的task，如果task已经在执行中，则返回false
print(task2.cancel())

time.sleep(3)
print(task1.done())

# result方法可以获取task的执行结果
print(task1.result())
print()

# 通过as_completed来获取执行结果
urls = [3, 2, 4]
all_tasks = [executor.submit(get_html, (url)) for url in urls]
wait(all_tasks, return_when=FIRST_COMPLETED)
print("main")
for future in as_completed(all_tasks):
    data = future.result()
    print(data)

print()
# 通过executor/map获取已经完成的task
for data in executor.map(get_html, urls):
    print(data)
