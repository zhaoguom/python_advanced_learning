# 线程间的通信
# 非线程安全，不推荐使用

import time
import threading


detail_url_list = []


def get_detail_html(detail_url_list):
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()

            print("get detail html starts, " + url)
            time.sleep(2)
            print("get detail html ends, " + url)


def get_detail_url(detail_url_list):
    while True:
        print("get detail url starts")
        time.sleep(3)
        for i in range(20):
            detail_url_list.append("http://projectsedu.com/{id}".format(id=i))
        print("get detail url ends")


if __name__ == "__main__":
    thread_detail_url = threading.Thread(
        target=get_detail_url, args=(detail_url_list,))
    thread_detail_url.start()
    for i in range(10):
        html_thread = threading.Thread(
            target=get_detail_html, args=(detail_url_list,))
        html_thread.start()
    start_time = time.time()
    print("last time: {}".format(time.time()-start_time))
