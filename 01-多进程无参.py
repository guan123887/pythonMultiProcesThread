# 1.导入进程包
from multiprocessing import Process
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
    # 2.通过进程类创建对象
    sing_process = Process(target=sing)
    dance_process = Process(target=dance)
    # 3.使用进程对象
    sing_process.start()
    dance_process.start()

