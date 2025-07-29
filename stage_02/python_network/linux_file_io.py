"""
字符串 <-> 字节串转换
所有字符串能转字节串
不是所有字节串都能转字符串

"""
# s = '你好'.encode() # 将字符串转换为字节串
# print(s)
# print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode()) # 将字节串转换为字符串


"""
file_open.py
文件打开方式
"""
# 打开文件
# f = open('a.py','r+') # 要求文件存在
# f = open('a.py','w') # 文件不存在创建存在清空
# f = open('a.py','a') # 文件不存在创建,存在追加
# f = open('a.py','rb') # 加b后续的读写都以字节串操作

# 所有文件都可以用二进制方式打开(b)
# 但是二进制格式文件则不能用文本方式打开(后续读写出错)
# try:
#     f  = open('aa.py','r',encoding='utf-8')
# except Exception as e:
#     print(e)

# 通过f 进行读写操作


"""
file_read.py
文件读取演示

"""
# 读取文件
# data = f.read()
# print(data)

# 循环读取文件内容
# while True:
#     # 如果读到文件结尾 read()会读到空字符串
#     data = f.read(10)
#     # 读到结尾跳出循环
#     if not data:
#         break
#     print(">",data)

# 读取文件一行内容
# data = f.readline(5) # 读取前5个字符
# print("一行内容:",data)
# data = f.readline() # 读完第一行剩余内容
# print("一行内容:",data)

# 读取内容形成列表
# data = f.readlines(35) # 读取至前35个字节所在的所有行
# print(data)
# data = f.readlines()
# print(data)

# 使用for循环读取每一行
# for line in f:
#     print(line)  # 每次迭代到一行内容

# 关闭 文件对象
# f.close()

# 练习 找单词打印解释内容
def find_word(word):
    with open('dict.txt', 'r', encoding='utf-8') as d:
        # 每次获取一行
        for line in d:
            w = line.split(' ')[0]
            # 如果遍历到的单词已经大于目标,就结束查找
            if w > word:
                return ("没有找到该单词")
            elif w == word:
                return line
        else:
            return "没有找到单词"


"""
file_write.py
文件写操作
"""
# e = open('aa.py', 'w',encoding='utf-8')
# e = open('11.jpg', 'wb') # 二进制
# e = open('aa.py', 'a',encoding='utf-8') # 追加

# 写操作
# e.write("hello 死鬼\n")
# e.write("哎呀,干啥\n")

# 将列表中每一项分别写入文件内
# l = ['hello world\n','hello kitty\n']
# e.writelines(l)
# e.close()


"""
练习 文件拷贝
将一个文件拷贝一份，文件可能是文本文件也可能是二进制文件
"""
# filename = input("File:")
# try:
#     fr = open(filename,'rb')  # 二进制文件操作
# except FileNotFoundError as e:
#     print(e)
# else:
#     fw = open('copy.txt','wb+')
#     #循环读写
#     while True:
#         data = fr.read(1024)
#         if not data:  # 读取结束
#             break
#         fw.write(data) # 将读取内容写入
#     fr.close()
#     fw.close()


"""
with.py
使用with 打开文件
"""
# # 生成文件对象f
# with open('a.py') as f:
#     data = f.read()
#     print(data)
# # with语句块结束 f 自动销毁


"""
buffer.py 缓冲区刷新测试
刷新缓冲区条件：
    缓冲区被写满
    程序执行结束或者文件对象被关闭
    行缓冲遇到换行
    程序中调用flush()函数
"""
# # f = open('a.py','w',1) # 行缓冲
# f = open('a.py','w')
# while True:
#     data = input(">>")
#     if not data:
#         break
#     f.write(data + '\n')
#     f.flush()  # 刷新缓冲区
# f.close()


"""
seek.py  文件偏移量测试
    tell() 获取偏移量
    seek(offset,whence) offset:负数前，正数后  whence:默认0头,1当前,2结尾，二进制打开不能为0
"""
# # 以r,w打开文件偏移量在开头，以a打开文件偏移量在结尾
# with open("bb.txt",'r+') as a:
#     print("文件偏移量:",a.tell())
#     a.read(5)
#     print("文件偏移量:",a.tell())
#     # 以开头为基准向后移动5个字符
#     a.seek(5,0)
#     a.write("&&&")


"""
    练习 插入时间 序号不断
"""
# import time
# j = open("bb.txt",'a+')
# j.seek(0,0)
# count = 0
# for line in j:
#     count += 1
# try:
#     while True :
#         count += 1
#         time.sleep(1)
#         str_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
#         j.write('%d. %s\n'%(count,str_time))
#         j.flush()
# except KeyboardInterrupt:
#     print("\n检测到 Ctrl + C，程序已结束。")

"""
文件描述符
    系统中每一个IO操作都会分配一个整数作为编号，该整数即这个IO操作的文件描述符。
"""
# # 获取对应的文件描述符
# f = open('aa.py','r')
# print(f.fileno())

""""
文件函数
"""
# import  os
# # 获取文件大小
# print(os.path.getsize('D:\\work\\PythonProject\\python_study\\stage_02\\aa.py'))
# # 查看文件列表
# print(os.listdir('./'))
# # 查看文件是否存在
# print(os.path.exists('./bb.txt'))
# # 判断文件类型
# print(os.path.isfile('./aa.txt'))
# # 删除文件
# os.remove('./bb.txt')
