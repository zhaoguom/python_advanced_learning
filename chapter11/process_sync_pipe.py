from multiprocessing import Process, Pipe
import time

# pipe的性能高于queue，只有两个进程的时候优先考虑pipe

def producer(pipe):
    pipe.send("zhaoguom")
    time.sleep(2)

def consumer(pipe):
    time.sleep(2)
    data = pipe.recv()
    print(data)

if __name__ == "__main__":
    receive_pipe, send_pipe = Pipe()
    # pipe只能适用于两个进程
    my_producer = Process(target=producer, args=(send_pipe,))
    my_consumer = Process(target=consumer, args=(receive_pipe,))

    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()


