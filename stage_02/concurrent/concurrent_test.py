"""
测试用例
"""
from multiprocessing import Process,Pool
from threading import Thread
import time

# # 装饰器
# def get_time(fun):
#     def wrapper(*args,**kwargs):
#         start_time = time.time()
#         result = fun(*args,**kwargs)
#         execute_time = time.time() - start_time
#         return execute_time
#     return wrapper

# 计算
def count(x,y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1

start_time = time.time()
for i in range(10):
    count(1,2)
execute_time = time.time() - start_time
print(execute_time) # 7.626738548278809

# 多进程
if __name__ == '__main__':
    start_time = time.time()
    pool = Pool(10)
    for i in range(10):
        pool.apply_async(func=count,args=(1,2))
    pool.close()
    pool.join()
    execute_time = time.time() - start_time
    print(execute_time) # 0.10601258277893066

# 多线程
if __name__ == '__main__':
    start_time = time.time()
    list1 = []
    for i in range(10):
        t = Thread(target=count,args=(1,2))
        list1.append(t)
        t.start()
    for i in list1:
        i.join()
    execute_time = time.time() - start_time
    print(execute_time) # 9.577175617218018


# IO
def write():
    with open('test', 'w') as f:
        for i in range(2000000):
            f.write("hello world\n")
def read():
    with open('test', 'r') as f:
        lines = f.readlines()
def io():
    write()
    read()

start_time = time.time()
for i in range(10):
    io()
execute_time = time.time() - start_time
print(execute_time) # 12.575918912887573


# 多进程
if __name__ == '__main__':
    start_time = time.time()
    pool = Pool(10)
    for i in range(10):
        pool.apply_async(func=io)
    pool.close()
    pool.join()
    execute_time = time.time() - start_time
    print(execute_time) # 2.831623077392578


# 多线程
if __name__ == '__main__':
    start_time = time.time()
    list1 = []
    for i in range(10):
        t = Thread(target=io)
        list1.append(t)
        t.start()
    for i in list1:
        i.join()
    execute_time = time.time() - start_time
    print(execute_time) # 17.13787317276001