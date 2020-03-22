# semaphore 用于控制进入数量的锁
# 文件，读/写，写一般只用于一个线程，读可以允许有多个线程

import threading
from threading import Semaphore
import time


class HtmlSpider(threading.Thread):

    def __init__(self, url, semaphore):
        super().__init__()
        self.url = url
        self.semaphore = semaphore

    def run(self):
        time.sleep(2)
        print("got html text success, " + self.url)
        self.semaphore.release()


class UrlProducer(threading.Thread):

    def __init__(self, semaphore):
        super().__init__()
        self.semaphore = semaphore

    def run(self):
        for i in range(20):
            self.semaphore.acquire()
            html_thread = HtmlSpider("https://www.baidu.com/{}".format(i), self.semaphore)
            html_thread.start()


if __name__ == "__main__":
    semephore = Semaphore(3)
    url_producer = UrlProducer(semephore)
    url_producer.start()
