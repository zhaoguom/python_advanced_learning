import asyncio
import time
from functools import partial

async def get_html(url):
    print("start to get url")
    await asyncio.sleep(2)
    return "zhaoguom"

def callback(url, future):
    print(url)
    print("send mail to zhaoguom")

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    task = loop.create_task(get_html("http://www.baidu.com"))
    # 需要的时候使用偏函数传入参数，因为add_done_callback本身不接收参数
    task.add_done_callback(partial(callback, "http://www.imooc.com"))
    loop.run_until_complete(task)

    print(task.result())
    print("elapsed time: {}".format(time.time()-start_time))