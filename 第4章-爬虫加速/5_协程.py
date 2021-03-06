import time


def func():
    print('hello')  # 让当前的线程处于阻塞状态，CPU是不工作的
    time.sleep(3)
    print('hello!!!')


if __name__ == '__main__':
    func()

# 一般情况下，当程序处于IO操作的时候，线程会处于阻塞状态
# 协程：当程序遇见IO操作时，可以选择性地切换到其他任务上
# 在微观上是一个任务一个任务的进行切换，切换条件一般就是IO操作
# 在宏观上，能看到的其实就是多个任务一起在执行
# 多任务异步操作
# 上面所讲的一切，都是在单线程的条件下
