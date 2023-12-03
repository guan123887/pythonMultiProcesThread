# 1.导入线程模块
from threading import Thread
import time


def sing(num1):
    for i in range(num1):
        print('唱歌...')
        time.sleep(0.5)


def dance(num2):
    for i in range(num2):
        print('跳舞...')
        time.sleep(0.5)


if __name__ == '__main__':
    # 2.通过线程类创建线程对象
    sing_thread = Thread(target=sing, args=(3,))
    dance_thread = Thread(target=dance, kwargs={'num2': 3})
    # 3.启动线程执行任务
    sing_thread.start()
    dance_thread.start()