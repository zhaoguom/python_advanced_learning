import asyncio
import aiohttp
from asyncio import Lock, Queue

cache = {}
lock = Lock()
queue = Queue()
async def get_stuff(url):
    # 也可以用这句with await lock:
    async with lock:
        # await lock.acquire()
        if url in cache:
            return cache[url]
        stuff = await aiohttp.request('GET', url)
        cache[url] = stuff
        # lock.release()
        return stuff

async def parse_stuff(url):
    _stuff = await get_stuff(url)
    # do something

async def use_stuff(url):
    _stuff = await get_stuff(url)
    # do something

url = "http://www.baidu.com"
tasks = [parse_stuff(url), use_stuff(url)]
pool = asyncio.get_event_loop()
pool.run_until_complete(asyncio.wait(tasks))

