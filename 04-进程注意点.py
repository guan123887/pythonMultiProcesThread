# 1.导入进程包

# 主进程会等待所有的子进程执行结束在结束,除非设置子进程守护主进程
from multiprocessing import Process
import time
import os


def work():
    # 子进程工作2s
    for i in range(10):
        print('工作中.....')
        time.sleep(0.2)


# 主进程
if __name__ == '__main__':
    work_process = Process(target=work);
    # 设置守护主进程,主进程退出后子进程直接销毁, 不再执行子进程中的代码
    work_process.daemon = True
    work_process.start()
    # 主进程睡眠1s
    time.sleep(1)
    print('主进程执行完毕')
