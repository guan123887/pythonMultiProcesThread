import time
from threading import Thread
# 主线程会等待所有子线程执行结束在结束,除非设置设置子线程守护主线程

def work():
    for i in range(10):
        print('工作...')
        time.sleep(2)


if __name__ == '__main__':
    # 设置子线程守护主线程
    # 方法一
    # sub_thread = Thread(target=work)
    # sub_thread.setDaemon(True)
    # sub_thread.start()

    # 方法二
    sub_thread = Thread(target=work, daemon=True)
    sub_thread.setDaemon(True)
    sub_thread.start()
    # 主线程等待1s,后结束
    time.sleep(1)
    print('主线程结束了...')
