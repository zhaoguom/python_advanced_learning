import time
import asyncio
from urllib.parse import urlparse
import socket

async def get_url(url):
    #通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    
    reader, writer = await asyncio.open_connection(host=host, port=80)
    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
    all_lines = []
    async for raw_line in reader:
        data = raw_line.decode("utf8")
        all_lines.append(data)
    
    html="".join(all_lines)
    return html

async def main(loop):
    tasks = []
    for url in range(50):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        tasks.append(asyncio.ensure_future(get_url(url)))
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    start_time = time.time()
    
    loop.run_until_complete(main(loop))
    print("elapsed time: {}".format(time.time()-start_time))
    