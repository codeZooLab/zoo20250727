"""
使用udp，从客户端录入学生信息，在服务端将学生信息写入文件
要求每个学生信息占一行
ID  NAME  AGE  SCORE
"""
from socket import *
import struct

sockfd = socket(AF_INET,SOCK_DGRAM)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('0.0.0.0',4567))
f = open("student.txt", 'a', encoding='utf-8')
while True:
    data,addr = sockfd.recvfrom(1024)
    # 定义数据传输格式 解包
    info = struct.unpack('i5sif',data)
    print(info)
    f.write('编号:%d,姓名:%s,年龄:%d,成绩:%.2f\r\n'%(info))
    f.flush()
f.close()
sockfd.close()