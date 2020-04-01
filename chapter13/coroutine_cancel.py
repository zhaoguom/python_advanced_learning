import asyncio
import time

async def get_html(sleep_time):
    print("start to get url")
    await asyncio.sleep(sleep_time)
    print("get url completed after {} seconds".format(sleep_time))


if __name__ == "__main__":
    task1 = get_html(2)
    task2 = get_html(3)
    task3 = get_html(3)
    tasks = [task1, task2, task3]
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        all_tasks = asyncio.Task.all_tasks()
        for task in all_tasks:
            print("cancel task")
            print(task.cancel())
        # 注意task cancel之后要stop loop并且重新启动loop，并且最后关闭
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()