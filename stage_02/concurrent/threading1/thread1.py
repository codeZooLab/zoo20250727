"""
thread1.py  线程基础使用
步骤： 1. 创建线程对象
      2. 启动线程
      3. 回收线程
"""

import os
from threading import Thread
from time import sleep,ctime

# a = 1
#
# # 线程函数
# def music():
#     global a
#     print("a = ",a)
#     a = 10000
#     for i in range(3):
#         sleep(2)
#         print(os.getpid(),"播放: 葫芦娃")
#
# # 线程对象
# t = Thread(target = music)
# t.start() # 启动线程
#
# for i in range(4):
#     sleep(1)
#     print(os.getpid(),"播放: 黄河大合唱")
#
# t.join() # 回收线程
# print("===========================")
# print("a:",a)


"""
thread_attr.py
线程属性示例
"""
# def fun():
#     sleep(3)
#     print("线程属性示例")
#
# t = Thread(target = fun,name = "Tarena")
# t.daemon = True # 主线程退出分支线程也退出
# t.start()
# t.name = "Tedu"
# print("Name:",t.name) # 线程名称
# print("is alive:",t.is_alive) # 是否在生命周期
# print("Daemon:",t.daemon)
# # t.join()



"""
自定义线程类
"""
# class ThreadClass(Thread):
#     def __init__(self, value):
#         self.value = value
#         super().__init__()  # 加载父类init
#
#     def f1(self):
#         print("步骤1")
#     def f2(self):
#         print("步骤2")
#
#     # 作为流程启动函数
#     def run(self):
#         for i in range(self.value):
#             self.f1()
#             self.f2()
#
# if __name__ == '__main__':
#     t = ThreadClass(1)
#     t.start()
#     t.join()


# 练习
class MyThread(Thread):
    # __init__可以添加参数，进行编写
    def __init__(self,target = None,args = (),kwargs = {}):
        super().__init__() # 此处不许传参
        self.target = target
        self.args = args
        self.kwargs = kwargs

    # 添加其他方法 run
    def run(self):
        if self.target:
            self.target(*self.args,**self.kwargs)

def player(sec,song):
    for i in range(3):
        print("Playing %s:%s"%(song,ctime()))
        sleep(sec)

if __name__ == '__main__':
    t = MyThread(target=player,args=(2,),kwargs={"song":"凉凉"})
    t.start()
    t.join()

