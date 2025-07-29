
from socket import *
import struct

sockfd = socket(AF_INET,SOCK_DGRAM)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# 服务端地址
ADDR = ('127.0.0.1',4567)
while True:
    id = int(input("编号:"))
    name = input("名称:")
    age = int(input("年龄:"))
    score = float(input("成绩:"))
    # 定义数据传输格式 数据打包
    data = struct.pack('i5sif',id,name.encode(),age,score)
    sockfd.sendto(data,ADDR)