from collections.abc import Awaitable
import types

async def downloader(url):
    return "zhaoguom"

@types.coroutine
def my_downloader(url):
    yield "zhaoguom"


async def download_url(url):
    #do something
    html = await downloader(url)
    return html


if __name__ == "__main__":
    coro = download_url("http://www.baidu.com")
    coro.send(None)