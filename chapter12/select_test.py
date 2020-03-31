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

# 使用非阻塞I/O完成html请求

def get_url(url):
    #通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((host, 80))
    except BlockingIOError:
        pass
    # 不停的询问连接是否建立好，需要while循环不停的去检查状态
    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
            break
        except OSError:
            pass

    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError:
            continue
        if d:
            data += d
        else:
            break
    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()

if __name__ == "__main__":
    get_url("http://www.baidu.com")