import asyncio
import time

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    return "zhaoguom"


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    
    # method #1
    future = asyncio.ensure_future(get_html("http://www.baidu.com"))
    loop.run_until_complete(future)
    print(future.result())

    # method #2: task是future的子类
    task = loop.create_task(get_html("http://www.baidu.com"))
    loop.run_until_complete(task)
    print(task.result())

    print(time.time()-start_time)