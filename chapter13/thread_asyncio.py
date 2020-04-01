from concurrent.futures import ThreadPoolExecutor
import asyncio
from urllib.parse import urlparse
import socket
import time

executor = ThreadPoolExecutor(3)

def get_url(url):
    #通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))

    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
    
    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()

if __name__ == "__main__":
    loop=asyncio.get_event_loop()
    start_time = time.time()
    tasks = []
    for url in range(50):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        task = loop.run_in_executor(executor, get_url, url)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print("time elapsed {}".format(time.time()-start_time))