# 1.导入进程包
from multiprocessing import Process
import time
import os


def sing(num, name):
    for i in range(num):
        print('唱歌进程的pid: ', os.getpid())
        print('唱歌进程父进程的pid: ', os.getppid())
        print('%s 唱歌...' % name)
        time.sleep(0.5)


def dance(num2, name2):
    for i in range(num2):
        print('跳舞进程的pid: ', os.getpid())
        print('跳舞进程的父进程pid: ', os.getppid())
        print(f'{name2} 跳舞...')
        time.sleep(0.5)


# 主进程
if __name__ == '__main__':
    print('主进程的pid: ', os.getpid())
    # 1.创建子进程对象并指定执行的任务名
    sing_process = Process(target=sing, args=(3, '小明',))
    dance_process = Process(target=dance, kwargs={'name2': '小红', 'num2': 3})
    # 2.启动子进程执行任务
    sing_process.start()
    dance_process.start()
