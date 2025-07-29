

from select import select
from socket import *

#　创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

"""
select示例
"""
# f = open('log.txt','r+')
#
# print("开始监控ＩＯ")
# rs,ws,xs = select([s],[f],[])
# print(rs)
# print(ws)
# print(xs)


"""
select tcp 服务
重点代码

思路分析:
1. 将关注的io放入监控列表
2. 当io就绪时通知select返回
3. 遍历返回值列表，处理就绪的io
"""
#　设置关注的io列表
rlist = [s]  #　ｓ　用于等待处理连接
wlist = []
xlist = []

#　循环io监控
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    # 遍历返回值列表，判断哪个io就绪
    for r in rs:
        if r is s:
            c,addr = r.accept()
            print("Connect from",addr)
            rlist.append(c) #　增加新的关注的io
        else:
            #　表明有客户端发送消息
            data = r.recv(1024).decode()
            # 客户端退出
            if not data:
                rlist.remove(r) # 取消对客户端的关注
                r.close()
                continue
            print(data)
            wlist.append(r)
    for w in ws:
        w.send(b'OK')
        wlist.remove(w) # 发完消息移除

    for x in xs:
        pass

