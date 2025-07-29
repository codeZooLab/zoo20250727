"""
 queue.py 消息队列演示
 注意：消息队列符合先进先出原则

"""
from multiprocessing import Process,Queue
from random import randint

def heand(q):
    for i in range(6):
        x = randint(1,33)
        q.put(x)  # 消息入队
    q.put(randint(1,16))

def request(q):
    l = []
    for i in range(6):
        l.append(q.get())  # 消息出队
    l.sort()
    l.append(q.get())
    print(l)

if __name__ == '__main__':
    # 创建消息队列
    q = Queue(5) # 最大长度5
    p1 = Process(target=heand,args=(q,))
    p2 = Process(target=request,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
