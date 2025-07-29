"""
httpserver v1.0
基本要求： 1. 获取来自浏览器的请求
         2. 判断请求内容是否为/
         3. 如果是，则将 index.html 发送给浏览器
            如果不是，则告知浏览器 sorry
         4. 注意组织http响应格式， 判断 200 or 404
"""

from socket import *

# 客户端处理
def request(connfd):
    # 获取请求 提取请求内容
    data = connfd.recv(1024)
    # 防止浏览器异常退出
    if not data:
        return
    requset_line = data.decode().split("\n")[0]
    info = requset_line.split(" ")[1]

    # 判断是/ 返回index.html 不是返回404
    if info == "/":
        with open('index.html',encoding='utf-8') as file:
            response = "HTTP/1.1 200 ok\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += file.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Sorry...</h1>"
    connfd.send(response.encode())

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(("0.0.0.0",8000))
sockfd.listen(5)
while True:
    connfd,addr = sockfd.accept()
    request(connfd) # 处理客户端请求