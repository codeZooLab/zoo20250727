"""
http server v2.0
env: python 3.6
IO多路复用 , http训练
"""

from socket import *
from select import *

# 具体功能服务
class HttpServer:
    def __init__(self,host,port,dir):
        self.host = host
        self.port = port
        self.dir = dir
        self.address = (host,port)
        # 直接创建出套接字
        self.create_socket()
        self.bind()
        # select 的监控列表
        self.rlist = []
        self.wlist = []
        self.xlist = []

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    # 绑定
    def bind(self):
        self.sockfd.bind(self.address)

    # 处理客户端请求
    def handle(self, connfd):
        # 接收http请求
        requrst = connfd.recv(1024)
        # 客户端断开
        if not requrst:
            self.rlist.remove(connfd)
            connfd.close()
            return
        # 提起请求内容 (将字节串按行切割)
        request_line = requrst.splitlines()[0]
        info = request_line.decode().split(' ')[1]
        print('请求内容:', info)
        # 根据请求内容进行数据整理
        # 分为两类: 1. 请求网页,2. 其他
        if info == '/' or info[-5:] == '.html':
            self.get_html(connfd,info)
        else:
            self.get_other(connfd,info)

    # 处理网页
    def get_html(self,connfd,info):
        if info == '/':
            # 请求主页
            filename = self.dir +'/index.html'
        else:
            filename = self.dir + info
        try:
            with open(filename, 'rb') as f:
                body = f.read()
            header = (
                b'HTTP/1.1 200 OK\r\n'
                b'Content-Type:text/html\r\n'
                b'\r\n')
            response = header + body
        # 网页不存在
        except Exception:
            response = (
                b'HTTP/1.1 404 Not Found\r\n'
                b'Content-Type:text/html\r\n'
                b'\r\n'
                b'<h1>Sorry....</h1>'
            )
        finally:
            # 讲内容发送给浏览器
            connfd.send(response)

    # 处理其他
    def get_other(self,connfd,info):
        with open(self.dir + info , 'rb') as f:
            body = f.read()
        header = (
                b'HTTP/1.1 200 OK\r\n'
                b'Content-Type:image/jpeg\r\n'
                b'\r\n')
        response = header + body
        connfd.send(response)

    # 启动入口
    def server_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %d"%(self.port))
        # 搭建IO多路服用监控各种IO请求
        self.rlist.append(self.sockfd)
        while True:
            rs,ws,xs = select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                # 浏览器连接进来
                if r is self.sockfd:
                    connfd,addr = self.sockfd.accept()
                    print("Connect from", addr)
                    self.rlist.append(connfd)
                else:
                    # 处理客户端请求
                    self.handle(r)

# 用户应该怎么用HTTPServer
if __name__ == "__main__":
    """
    通过HTTPServer快速启动服务,用于展示自己的网页
    """
    # 需要用户自己决定的内容
    HOST = '0.0.0.0'
    PORT = 8000
    # 网页存储位置
    # DIR = 'D:\chengxu\python\PythonProjects\python_study\stage_02\concurrent\io\static'
    DIR ='/home/zzl/python_project/python_study/stage_02/concurrent/io/static'
    httpd = HttpServer(HOST,PORT,DIR)
    httpd.server_forever() # 服务启动入口