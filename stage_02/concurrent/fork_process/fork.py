"""
fork.py  fork进程创建演示
    fork liunx系统支持
"""
import os,sys
from time import sleep
import signal

# # 创建子进程
# pid = os.fork()  # pid为新建进程的pid,新的进程(子进程)pid为0
#
# if pid < 0:
#     print("Create fork_process failed")
# elif pid == 0:
#     # 只有子进程执行
#     sleep(3)
#     print("The new fork_process")
# else:
#     # 只有父进程执行
#     sleep(4)
#     print("The old fork_process")
#
# # 父子进程都执行
# print("fork_process test over")


"""
fork1.py fork进程演示细节
"""
# print("=========================") # 子进程只从fork下一句开始执行，该打印只在主进程执行
# a = 1   # 子进程会复制父进程全部内存空间
# def fun():
#     print("fun .... ")
#
# pid = os.fork()
#
# if pid < 0:
#     print("Create fork_process failed")
# elif pid == 0:
#     print("Child fork_process")
#     print("a = ",a)  # 从父进程空间拷贝了变量
#     fun()
#     a = 10000  # 只是修改了自己空间的a
# else:
#     sleep(1)
#     print("Parent fork_process")
#     print("a:",a)
#
# print("All a ->",a)  # 父子进程都会执行


"""
获取进程PID号
"""
# pid = os.fork()
#
# if pid < 0:
#     print("Error")
# elif pid == 0:
#     # sleep(1) 通过sleep 让父进程先结束 从而子进程变为孤儿进程
#     print("Child PID:",os.getpid()) # 自己pid
#     print("Get parent PID:",os.getppid()) # 父pid
# else:
#     print("Parent PID:", os.getpid())  # 自己pid
#     print("Get child PID:",pid)


"""
进程退出演示
"""
# pid = os.fork()
#
# # 父子进程退出不会影响对方继续执行
# if pid < 0:
#     print("Error")
# elif pid == 0:
#     os._exit(0) # 子进程退出
#     print("Child fork_process")
# else:
#     sys.exit("退出父进程") # 子进程退出
#     print("Parent fork_process")


"""
模拟僵尸进程产生
    os.wait() 处理僵尸
    信号处理僵尸 signal.signal(signal.SIGCHLD,signal.SIG_IGN)
"""
# # 忽略子进程的退出行为，子进程退出自动由系统处理
# signal.signal(signal.SIGCHLD,signal.SIG_IGN)
#
# pid = os.fork()
# if pid < 0:
#     print("Error")
# elif pid == 0:
#     print("Child PID:",os.getpid())
#     sys.exit(2)
# else:
#     """
#     os.wait() 处理僵尸 在父进程中阻塞等待处理子进程退出
#     wait是阻塞函数,子进程不结束无法执行父进程后续逻辑,导致无法实现开多进程并发处理的预期，所以一般不用
#     """
#     # pid,status = os.wait()
#     # print("pid:",pid)
#     # print('status:',os.WEXITSTATUS(status))
#     while True: # 让父进程不退出
#         pass


"""
创建二级子进程处理僵尸
"""
# def f1():
#     sleep(2)
#     print("写代码")
#
# def f2():
#     sleep(4)
#     print("测代码")
#
# pid = os.fork()
# if pid == 0:
#     p = os.fork()  # 创建二级子进程
#     if p == 0:
#         f1()
#     else:
#         os._exit(0)  # 一级子进程退出
# else:
#     os.wait()  # 等待回收一级子进程
#     f2()e