"""
Process 创建进程演示
1. 编写进程函数
2. 生成进程对象
3. 启动进程
4. 回收进程
"""

import multiprocessing as mp
import os,time

# a = 1
#
# # 进程执行函数
# def fun():
#     print("开始一个进程")
#     time.sleep(2)
#     global a
#     print("a = ",a)
#     a = 10000
#     print("子进程结束")
#
# if __name__ == '__main__':
#     # 创建进程对象
#     p = mp.Process(target = fun)
#     # 启动进程
#     p.start()
#
#     # 父进程执行事件
#     time.sleep(3)
#     print("父进程干点事")
#
#     # 回收进程
#     p.join()
#
#     print("a:",a)
"""
上面如同以下代码：
    pid = os.fork()
    if pid == 0:
        fun()
        os._exit()
    else:
        os.wait()
"""


"""
创建多个子进程
"""
# def th1():
#     time.sleep(3)
#     print("吃饭")
#     print(os.getppid(),'--',os.getpid())
# def th2():
#     time.sleep(2)
#     print("睡觉")
#     print(os.getppid(),'--',os.getpid())
# def th3():
#     time.sleep(4)
#     print("打豆豆")
#     print(os.getppid(),'--',os.getpid())
#
# if __name__ == '__main__':
#     things = [th1,th2,th3]
#     jobs = []
#
#     for th in things:
#         p = mp.Process(target=th)
#         jobs.append(p)  # 对进程对象进行存储
#         p.start()
#
#     # [i.join() for i in jobs]
#     # 一起回收
#     for i in jobs:
#         i.join()


"""
Process 给进程函数传参
"""
# # 含有参数的进程函数
# def worker(sec,name):
#     for i in range(3):
#         time.sleep(sec)
#         print("I'm %s"%name)
#         print("I'm working...")
#
# if __name__ == '__main__':
#     # 通过args 给函数位置传参
#     # p = mp.Process(target=worker,args=(2,'Levi'))
#     p = mp.Process(target=worker,args=(2,),kwargs={'name':'Baron'})
#     p.start()
#     p.join()


"""
进程对象属性
"""
# def tm():
#     for i in range(3):
#         print(time.ctime())
#         time.sleep(2)
#
# if __name__ == '__main__':
#     p = mp.Process(target = tm,name = 'Tarena')
#     # p.daemon = True # 父进程退出，其所有子进程也退出
#     p.start()  # 进程真正产生
#     print("Name:",p.name)  # 进程名
#     print("PID：",p.pid) # pid号
#     print("is alive:",p.is_alive()) # 是否在生命周期



# 练习1 将一个文件拆分两部分 多进程写入文件
size = os.path.getsize('pool.py')
split_point = size // 2

def top_file():
    with open('pool.py', 'rb') as f:
        data = f.read(split_point)
    with open('top.txt','wb') as d:
        d.write(data)

def bot_file():
    with open('pool.py', 'rb') as f:
        f.seek(split_point,1)
        data = f.read()
    with open('bot.txt','wb') as d:
        d.write(data)

if __name__ == '__main__':
    p1 = mp.Process(target=top_file)
    p2 = mp.Process(target=bot_file)
    p1.start()
    p2.start()
    p1.join()
    p2.join()