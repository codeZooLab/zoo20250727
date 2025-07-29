"""
ftp 文件服务, 客户端
"""

import sys,time
from socket import *
from threading import Thread

# 服务器地址
ADDR = ('127.0.0.1', 8080)

# 文件处理类
class FTPClient:
    # 所有函数都使用sockfd,所以把它变为属性变量
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b'L') # 发送请求
        # 等待回复 (服务端能否满足请求)
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            # 一次性接收所有文件
            data = self.sockfd.recv(4096).decode()
            print(data)
        else:
            print(data)

    def do_quit(self):
        self.sockfd.send(b'Q') # 退出请求
        self.sockfd.close()
        sys.exit("谢谢使用")

    def do_get(self,filename):
        # 发送请求
        self.sockfd.send(('G '+filename).encode())
        # 等待回复
        data = self.sockfd.recv(127).decode()
        if data == "OK":
            with open(filename,'wb') as f:
                # 循环接收内容,写入文件
                while True:
                    data = self.sockfd.recv(1024)
                    if data == b'##': # 发送完成
                        break
                    f.write(data)
        else:
            print(data)

    def do_put(self,filename):
        try:
            with open(filename,'rb') as f:
                filename = filename.split('/')[-1]
                self.sockfd.send(('P ' + filename).encode())
                data = self.sockfd.recv(128).decode()
                if data == "OK":
                    while True:
                        data = f.read(1024)
                        if not data:
                            time.sleep(0.2)
                            self.sockfd.send(b'##')
                            break
                        self.sockfd.send(data)
                else:
                    print(data)
        except Exception as e:
            print("文件不存在")
            return
# 启动函数
def main():
    s = socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print(e)
        return

    ftp = FTPClient(s) # 实例化对象,用于调用功能
    # 循环发送请求给服务器
    while True:
        print("""\n
          =========Command============
          ****       list        ****
          ****    get   file     ****
          ****    put   file     ****
          ****       quit        ****
          ============================
        """)

        cmd = input("请输入选项:")
        if cmd.strip() == 'list':
            ftp.do_list()
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        elif cmd.strip()[:3] == 'get':
            filename = cmd.strip().split(' ')[-1]
            ftp.do_get(filename)
        elif cmd.strip()[:3] == 'put':
            filename = cmd.strip().split(' ')[-1]
            ftp.do_put(filename)
        else:
            print("请输入正确命令")

if __name__ == '__main__':
    main()