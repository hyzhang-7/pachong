from multiprocessing import Process


# 也有两个写法，和多线程写法一样


# def func():
#     for i in range(100000):
#         print('子进程', i)
#
#
# if __name__ == '__main__':
#     t = Process(target=func)
#     t.start()
#     for i in range(100000):
#         print('主进程', i)


def func1(name):
    for i in range(100000):
        print(name, i)


# 创建两个进程且传入参数
if __name__ == '__main__':
    t1 = Process(target=func1, args=('周杰伦',))  # 传递参数必须是元组
    t1.start()

    t1 = Process(target=func1, args=('王力宏',))
    t1.start()

    for i in range(100000):
        print('主进程', i)
