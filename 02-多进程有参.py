# 1.导入进程包
from multiprocessing import Process
import time


def sing(num, name):
    for i in range(num):
        print('%s 唱歌...' % name)
        time.sleep(0.5)


def dance(num2, name2):
    for i in range(num2):
        print(f'{name2} 跳舞...')
        time.sleep(0.5)


if __name__ == '__main__':
    # 2.通过进程类创建对象
    # 元组方式传参  args  参数位置需要一一对应  注意,一个参数时要写成 args=(name,)  最后有个逗号
    sing_process = Process(target=sing, args=(3, '小明',))
    # 字典方式传参    kwargs  指定key 不需要一一对应
    dance_process = Process(target=dance, kwargs={'name2': '小红', 'num2': 3})
    # 3.使用进程对象
    sing_process.start()
    dance_process.start()

