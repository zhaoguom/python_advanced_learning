import asyncio
import re
import aiohttp
import aiomysql
from pyquery import PyQuery

start_url = "http://jobbole.com/licai/"
waiting_urls = []
seen_urls = set()
stopping = False

async def fetch(url, session):
    async with session.get(url) as response:
        data = await response.text()
        print(data)
        return data

async def article_handler(url, session, pool):
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)
    pq = PyQuery(html)
    title = pq("title").text()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("insert into spider(title) values('{}')".format(title))


def extract_urls(html):
    urls = []
    pq = PyQuery(html)
    for link in pq.items("a"):
        url = link.attr("href")
        if url and url.startswith("/licai/yh") and url not in seen_urls:
            urls.append("http://jobbole.com" + url)
            waiting_urls.append(url)
    return urls

async def init_urls(url, session):
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)


async def main(loop):
    pool = await aiomysql.create_pool(host='192.168.1.200', port=3306, user='root',password='root',
                                    db='mxshop',loop=loop, charset='utf8', autocommit=True)
    async with aiohttp.ClientSession() as session:
        html = await fetch(start_url, session)
        seen_urls.add(start_url)
        extract_urls(html)
    asyncio.ensure_future(consumer(pool))

async def consumer(pool):
    async with aiohttp.ClientSession() as session:

        while not stopping:
            if len(waiting_urls)==0:
                await asyncio.sleep(0.5)
                continue

            url = waiting_urls.pop()
            print("start get url: {}".format(url))
            if re.match('/licai/yh/\d+', url):
                url = "http://jobbole.com" + url
                if url not in seen_urls:
                    asyncio.ensure_future(article_handler(url, session, pool))
            else:
                url = "http://jobbole.com" + url
                if url not in seen_urls:
                    asyncio.ensure_future(init_urls(url, session))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()