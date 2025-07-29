"""
pipe.py 管道操作
注意： 1. multiprocessing中提供的通信只用于亲缘关系进程间通信
     2. 管道在父进程中创建，子进程从父进程中获取管道对象
"""
from multiprocessing import Process,Pipe

def app1(fd1):
    print("启动app1，请登录")
    print("请求app2授权")
    # 写管道
    fd1.send("app1 可以用你的账号登录吗？")
    data = fd1.recv()
    if data:
        print("登录成功：",data)

def app2(fd2):
    request = fd2.recv() # 阻塞等待读取管道
    print(request)
    fd2.send(('Joy','123')) # 发送python数据类型

if __name__ == '__main__':
    # 创建管道对象
    # 参数true,False表示单向管道 fd1只能recv,fd2只能send
    fd1, fd2 = Pipe()
    p1 = Process(target=app1,args=(fd1,))
    p2 = Process(target=app2,args=(fd2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

