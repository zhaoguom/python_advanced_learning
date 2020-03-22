import time
import threading


def get_detail_html(url):
    print("get detail html starts")
    time.sleep(2)
    print("get detail html ends")


def get_detail_url(url):
    print("get detail url starts")
    time.sleep(3)
    print("get detail url ends")


if __name__ == "__main__":
    thread1 = threading.Thread(target=get_detail_html, args=("", ))
    thread2 = threading.Thread(target=get_detail_url, args=("", ))
    # 设置守护线程，当主线程退出的时候，该线程立即退出
    thread1.setDaemon(True)
    thread2.setDaemon(True)
    start_time = time.time()

    thread1.start()
    thread2.start()
    # 等待线程执行完成，再往下执行
    thread1.join()
    thread2.join()
    print("last time: {}".format(time.time()-start_time))
