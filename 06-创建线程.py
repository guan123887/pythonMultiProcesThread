# 1.导入线程模块
from threading import Thread
import time


def sing():
    for i in range(3):
        print('唱歌...')
        time.sleep(0.5)


def dance():
    for i in range(3):
        print('跳舞...')
        time.sleep(0.5)


if __name__ == '__main__':
    # 2.通过线程类创建线程对象
    sing_thread = Thread(target=sing)
    dance_thread = Thread(target=dance)
    # 3.启动线程执行任务
    sing_thread.start()
    dance_thread.start()