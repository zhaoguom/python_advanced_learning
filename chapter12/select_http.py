'''
Unix下5中I/O模型
阻塞式I/O
非阻塞式I/O
I/O复用
信号驱动式I/O - 这个用的少
异步I/O(POSIX的aio_系列函数)
'''

# 在并发高，连接活跃度不是很高的情况下，epoll比select好 
# 在并发不是很高，连接活跃度很高的情况下，select比epoll好

import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

#使用select完成http请求
selector = DefaultSelector()
stop = False
urls = ["http://www.baidu.com"]

class Fetcher:
    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)
    
    def readable(self, key):
        
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            global stop
            stop = True

    def get_url(self, url):
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b''
        if self.path == "":
            self.path = "/"
        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))
        except BlockingIOError:
            pass

        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)

def loop():
    #1. select本身不支持register模式
    #2. socket状态变化以后的回调是由程序员来完成的
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)

if __name__ == "__main__":
    fetcher = Fetcher()
    fetcher.get_url("http://www.baidu.com")
    loop()