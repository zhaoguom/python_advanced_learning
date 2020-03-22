# 条件变量，用于复杂的线程锁

from threading import Condition, Lock
import threading

class XiaoAi(threading.Thread):
    def __init__(self, condition):
        super().__init__(name="XiaoAI")
        self.condition = condition
    
    def run(self):
        with self.condition:
            self.condition.wait()
            print("{}: 在".format(self.name))
            self.condition.notify()

            self.condition.wait()
            print("{}: 好啊".format(self.name))
            self.condition.notify()

            self.condition.wait()
            print("{}: 君住长江尾".format(self.name))
            self.condition.notify()


class TianMao(threading.Thread):
    def __init__(self, condition):
        super().__init__(name="TianMao")
        self.condition = condition
    
    def run(self):
        with self.condition:
            print("{}: 小爱同学".format(self.name))
            self.condition.notify()
            self.condition.wait()

            print("{}: 我们来对古诗吧".format(self.name))
            self.condition.notify()
            self.condition.wait()

            print("{}: 我住长江头".format(self.name))
            self.condition.notify()
            self.condition.wait()

if __name__ == "__main__":
    condition = Condition()
    xiaoai = XiaoAi(condition)
    tianmao= TianMao(condition)
    
    xiaoai.start()
    tianmao.start()

