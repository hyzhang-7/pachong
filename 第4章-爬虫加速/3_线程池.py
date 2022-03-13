# 线程池：一次性开辟一些线程，用户直接给线程池子提交任务，线程任务的调度交给线程池来完成
# 导入线程池和进程池
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def func(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':
    # 创建线程池，共50个线程
    with ThreadPoolExecutor(50) as t:
        for i in range(100):  # 100个任务
            t.submit(func, name=f'任务{i}')
    # with会等待线程池的中任务全部执行完毕，才能继续执行
    print('over')

# 如果要使用进程池，把ThreadPoolExecutor改为ProcessPoolExecutor即可
