import asyncio
import time

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("get url completed")


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html("http://www.baidu.com") for _ in range(10)]
    # 提交一个协程
    loop.run_until_complete(get_html("http://www.baidu.com"))
    # 提交一组协程
    loop.run_until_complete(asyncio.wait(tasks))
    
    print(time.time()-start_time)