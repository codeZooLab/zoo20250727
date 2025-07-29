"""
value.py 开辟共享内存空间
注意： 共享内存中只能有一个值
"""
from multiprocessing import Process,Value,Array
import time
import random

# # 创建共享内存
# money = Value('i',5000)
#
# def man():
#     for i in range(30):
#         time.sleep(0.2)
#         # 修改共享内存
#         money.value += random.randint(1,1000)
#
# def girl():
#     for i in range(30):
#         time.sleep(0.15)
#         money.value -= random.randint(100,800)
# if __name__ == '__main__':
#     p1 = Process(target=man)
#     p2 = Process(target=girl)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print("一个月余额：",money.value) #读取共享内存



"""
array.py
共享内存中存放列表，字节串
"""
# 创建共享内存，初始数据 [1,2,3,4]
# shm = Array('i',[1,2,3,4])
# shm = Array('i',4) # 开辟4个整形的列表空间
shm = Array('c',b'hello')

def fun():
    # 共享内存对象可以迭代
    for i in shm:
        print(i)
    shm[0] = b'H' # 修改共享内存

if __name__ == '__main__':
    p = Process(target=fun)
    p.start()
    p.join()
    for i in shm:
        print(i)
    print(shm.value) # 整体打印字节串


