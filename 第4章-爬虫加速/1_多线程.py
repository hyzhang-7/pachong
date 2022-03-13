""""
进程是资源单位，每个进程至少要有一个线程
线程是执行单位

"""

# 启动每一个程序默认都会有一个主线程
# if __name__ == '__main__':
#     print('hello')

# 多线程
from threading import Thread


def func():
    for i in range(5):
        print('func', i)


# 多线程用法一
if __name__ == '__main__':
    t = Thread(target=func)  # 创建线程并给线程安排任务
    t.start()  # 多线程状态为可以开始工作状态，具体的执行时间有CPU决定
    for i in range(5):
        print('main', i)

# 多线程用法二
from threading import Thread


class MyThread(Thread):
    # 重写run方法
    def run(self):
        for i in range(100):
            print('子线程', i)


if __name__ == '__main__':
    t = MyThread()
    t.start()

    for i in range(100):
        print('主线程', i)
