"""
ftp 文件服务器 ,服务端
env: python 3.6
多进程多线程并发 socket
"""

import os,time
import sys,signal
from socket import *
from threading import Thread

# 全局变量
ADDR = ('0.0.0.0',8080)
FTP = "/home/zzl/python_project/python_study/stage_02/concurrent/threading1/" # 文件库路径

# 功能类 (线程类)
# 查文档, 下载,上传
class FTPServer(Thread):
    def __init__(self,connfd):
        super().__init__()
        self.connfd = connfd

    # 处理文件列表
    def do_list(self):
        files = os.listdir(FTP)
        if not files:
            self.connfd.send('文件库为空'.encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.2)
        # 拼接文件
        filelist = ''
        for file in files:
            if file[0] != '.' and os.path.isfile(FTP+file):
                filelist += file + '\n'
        self.connfd.send(filelist.encode())

    def do_get(self,filename):
        try:
            with open(FTP+filename,'rb') as f:
                self.connfd.send(b'OK')
                time.sleep(0.2)
                while True:
                    data = f.read(1024)
                    if not data:
                        time.sleep(0.2)
                        self.connfd.send(b'##')
                        break
                    self.connfd.send(data)
        except Exception:
            self.connfd.send("文件不存在".encode())
            return

    def do_put(self,filename):
        if os.path.exists(FTP+filename):
            self.connfd.send("文件已存在".encode())
            return
        else:
            self.connfd.send(b'OK')
        with open(FTP+filename,'wb') as f:
            while True:
                data = self.connfd.recv(1024)
                if data == b'##':
                    break
                f.write(data)

    # 循环接受来自客户端的请求
    def run(self):
        while True:
            request = self.connfd.recv(1024).decode()
            if not request or request == 'Q':
                return # 线程退出
            elif request == 'L':
                self.do_list()
            elif request[0] == 'G':
                filename = request.split(' ')[-1]
                self.do_get(filename)
            elif request[0] == 'P':
                filename = request.split(' ')[-1]
                self.do_put(filename)

# 启动函数
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(10)
    print("Listen the port 8080....")
    while True:
        # 循环等待客户端连接
        try:
            c,addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            sys.exit("服务端退出")
        except Exception as e:
            print(e)

        # 创建新的线程处理请求
        client = FTPServer(c)
        client.daemon = True
        client.start()


if __name__ == '__main__':
    main()