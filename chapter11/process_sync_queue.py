from multiprocessing import Process, Queue
import time


def producer(queue):
    queue.put("a")
    time.sleep(2)

def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)

if __name__ == "__main__":
    queue = Queue()
    my_procuder = Process(target=producer, args=(queue,))
    my_consumer = Process(target=consumer, args=(queue,))
    my_procuder.start()
    my_consumer.start()
    my_procuder.join()
    my_consumer.join()
    
