import time
import asyncio
from asyncio import ALL_COMPLETED,FIRST_COMPLETED
from random import randint

async def get_html(url):
    print("start to get url")
    await asyncio.sleep(2)
    print("get url completed")
    return "zhaoguom"


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html("http://www.baidu.com") for _ in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks))
    loop.run_until_complete(asyncio.gather(*tasks))
    print("time elapsed: {}".format(time.time()-start_time))

    # gather 和 wait的区别， gather更加high level，可以对任务进行分组
    group1 = [get_html("http://www.baidu.com") for _ in range(10)]
    group2 = [get_html("http://www.google.com") for _ in range(10)]
    # loop.run_until_complete(asyncio.gather(*group1, *group2))
    
    # or:
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)
    # group1.cancel()
    # group2.cancel()

    loop.run_until_complete(asyncio.gather(group1, group2))
    
