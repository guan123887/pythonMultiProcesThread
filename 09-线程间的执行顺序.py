# 线程之间执行顺序是无序的
import threading
from threading import Thread
import time


def work():
    time.sleep(1)
    thread = threading.current_thread()
    print(thread)


if __name__ == '__main__':
    for i in range(5):
        # 打印结果表明顺序时无序的,由CPU调度决定
        sub_thread = Thread(target=work)
        sub_thread.start()