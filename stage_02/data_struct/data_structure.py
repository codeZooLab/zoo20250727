
"""
linklist 线性表的链式存储
功能：实现单链表的构建和功能操作

"""
# 创建节点类
class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

# node1 = Node(1)
# node2 = Node(2,node1)
# node3 = Node(3,node2)

class LinkList:
    """
    思路 : 生成单链表,通过实例化的对象就代表一个链表
          可以调用具体的操作方法完成各种功能
    """
    def __init__(self):
        # 链表的初始化节点,没有有用数据,但是便于标记链表的开端
        self.head = Node(None)

    # 初始化链表,添加一组节点
    def init_list(self,list_):
        p = self.head  # p 作为移动变量
        for i in list_:
            # 遍历到一个值就创建一个节点
            p.next = Node(i)
            p = p.next

    # 遍历链表
    def show(self):
        p = self.head.next  # p代表第一个有值的节点
        while p is not None:
            print(p.val)
            p = p.next  # p向后移动

    # 判断链表为空
    def is_empty(self):
        if self.head.next is None:
            return True
        return False

    # 清空链表
    def clear(self):
        self.head.next = None

    # 尾部插入
    def append(self,val):
        p = self.head
        # p移动到最后一个节点
        while p.next is not None:
            p = p.next
        p.next = Node(val) # 最后添加节点

    # 头部插入
    def head_insert(self,val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

    # 指定位置插入
    def insert(self,index,val):
        # 设置个p 移动到待插入位置的前一个
        p = self.head
        for i in range(index):
            # 如果index超出了最大范围跳出循环
            if p.next is None:
                break
            p = p.next
        # 插入节点
        node = Node(val)
        node.next = p.next
        p.next = node

    # 删除节点
    def remove(self,val):
        p = self.head
        # p 移动,待删除节点上一个
        while p.next is not None and p.next.val != val:
            p = p.next

        if p.next is None:
            raise ValueError("x not in linklist")
        else:
            p.next = p.next.next

    # 获取某个节点的值 (通过索引获取)
    def search(self,index):
        if index < 0:
            raise IndexError("index out of range")

        p = self.head.next
        # 循环移动p
        for i in range(index):
            if p is None:
                raise IndexError("index out of range")
            p = p.next
        return p.val

    def merge(self,L1,L2):
        """
        给出两个有序的链表L1,L2 .
        在不创建新的链表的基础上将两个链表合并为一个
        要求合并后的链表仍为有序
        """
        # 将L2向L1中合并
        p = L1.head
        q = L2.head.next
        while p.next is not None:
            if p.next.val < q.val:
                p = p.next
            else:
                tmp = p.next
                p.next = q
                p = p.next
                q = tmp
        p.next = q


# if __name__ == "__main__":
#     # 链表操作
#     # l = LinkList()
#     # l.init_list([3,5,8,10,1])
#     # l.clear()
#     # l.append(100)
#     # l.head_insert(88)
#     # l.insert(8,99)
#     # l.show()
#     # print(l.search(2))
#
#     # 链表合并
#     l1 = LinkList()
#     l2 = LinkList()
#     l1.init_list([1,3,8,9,20])
#     l2.init_list([0,6,7,11])
#     l1.merge(l1,l2)
#     l1.show()
#     print("==================")
#     l2.show()


"""
sstack.py  栈模型的顺序存

思路 :
1. 顺序存储可以使用列表实现,但是列表功能丰富,不符合栈模型要求
2. 将列表功能封装,实现顺序栈的类,只提供栈的操作功能

功能: 出栈, 入栈,判断栈空,查看栈顶元素
"""
# 自定义异常
class StackError(Exception):
    pass

# 顺序栈
class SStack:
    def __init__(self):
        # 空列表就是栈的存储空间
        # 列表的最后一个元素作为栈顶元素
        self.__elems = []

    # 入栈
    def push(self,val):
        self.__elems.append(val)

    # 判断栈空
    def is_empty(self):
        return self.__elems == []

    # 出栈
    def pop(self):
        if self.is_empty():
            raise StackError("pop from empty stack")
        # pop:剔除并返回元素 默认最后一个
        return self.__elems.pop()

    # 查看栈顶
    def top(self):
        if self.is_empty():
            raise StackError("pop from empty stack")
        return self.__elems[-1]


# if __name__ == '__main__':
#     # 栈操作
#     # st = SStack()
#     # st.push(10)
#     # st.push(20)
#     # st.push(30)
#     # while not st.is_empty():
#     #     print(st.pop())
#
#     # 逆波兰表达式练习
#     st = SStack()
#     ops = {
#         '+': 'st.push(x + y)',
#         '-': 'st.push(x - y)',
#         '*': 'st.push(x * y)',
#         '/': 'st.push(x / y)'
#     }
#     while True:
#         exp = input()
#         tmp = exp.split(' ')  # 按照空格切割字符串
#         for i in tmp:
#             if i not in ops and i != 'p':
#                 st.push(float(i))
#             elif i in ops:
#                 y = st.pop()
#                 x = st.pop()
#                 exec(ops[i])
#             elif i == 'p':
#                 print(st.top())


"""
lstack.py 栈的链式模型

思路:
1. 通过节点存储数据达到链式存储的目的
2. 封装方法,实现栈的基本操作(入栈,出栈,栈空,查看栈顶)
3. top为栈顶,在链表的头作为栈顶位置 (不许要遍历)
"""
# 链式栈模型
class LStack:
    def __init__(self):
        # top作为栈顶的标记
        self.__top = None

    def is_empty(self):
        return self.__top is None

    # 入栈
    def push(self, val):
        self.__top = Node(val, self.__top)

        # node = Node(val)
        # node.next = self.__top
        # self.__top = node

    # 出栈
    def pop(self):
        if self.is_empty():
            raise StackError("pop from empty stack")
        data = self.__top.val
        self.__top = self.__top.next
        return data

    # 查看栈顶元素
    def top(self):
        if self.is_empty():
            raise StackError("pop from empty stack")
        return self.__top.val

# if __name__ == '__main__':
#     ls = LStack()
#     ls.push(10)
#     ls.push(20)
#     ls.push(30)
#     print(ls.top())
#     print(ls.pop())


"""
squeue.py  队列的顺序存储

思路 :
1. 基于列表完成数据存储
2. 对列表功能进行封装
3. 列表的头部作为队头,尾部作为队尾
功能: 入队(enqueue),出队(dequeue),判断队列为空
"""
# 自定义异常
class QueueError(Exception):
    pass

class SQueue:
    def __init__(self):
        self.__elems = []

    def is_empty(self):
        return self.__elems == []

    # 入队
    def enqueue(self,val):
        self.__elems.append(val)

    # 出对
    def dequeue(self):
        if self.is_empty():
            raise QueueError("Queue is empty")
        return self.__elems.pop(0)

# if __name__ == '__main__':
#     #
#     sq = SQueue()
#     sq.enqueue(10)
#     sq.enqueue(20)
#     sq.enqueue(30)
#     print(sq.dequeue())
#     print(sq.dequeue())
#
#     """
#     创建一个顺序队列, 队列中入队一组值
#     将队列中的值反转过来(值的个数不确定).
#     比如:[1,2,3,4,5]-->[5,4,3,2,1]
#     """
#     sq = SQueue()
#     for i in range(8):
#         sq.enqueue(i)
#     # 完成队列反转
#     ls = LStack()
#     # 出队 入栈
#     while not sq.is_empty():
#         ls.push(sq.dequeue())
#     # 出栈 入队
#     while not ls.is_empty():
#         sq.enqueue(ls.pop())
#     while not sq.is_empty():
#         print(sq.dequeue())


"""
lqueue.py 链式队列

思路:
1. 基于链表构建队列模型
2. 链表的开端作为队头, 结尾作为队尾
3. 对头队尾分别添加标记,避免每次插入数据都遍历链表
4. 队头和队尾重叠时认为队列为空
"""
# 队列操作
class LQueue:
    def __init__(self):
        # 定义队头,队尾
        self.front = self.rear = Node(None)

    def is_empty(self):
        return self.front == self.rear

    # 入队  rear动
    def enqueue(self,val):
        self.rear.next = Node(val)
        self.rear = self.rear.next

    # 出队  front动
    def dequeue(self):
        if self.front == self.rear:
            raise QueueError("Queue is empty")

        # front移动到的节点已经出队
        self.front = self.front.next
        return self.front.val

# if __name__ == '__main__':
#     lq = LQueue()
#     lq.enqueue(10)
#     lq.enqueue(20)
#     lq.enqueue(30)
#     print(lq.dequeue())


"""
编写一个接口程序,要求判断一段文字中括号匹配是否正确,
如果正确则打印"匹配正确",如果不正确则打印出哪里出错(只需要找出第一个错误即可)

出错情况 : 少前括号,少后括号,括号不匹配

def is_balanced_parentheses(text):
    stack = []
    map = {'}':'{',']':'[',')':'('}

    for char in text:
        if char in map.values():
            stack.append(char)
        elif char in map.keys():
            if not stack or stack.pop() != map[char]:
                return  False
    return len(stack) == 0
text = '{[]}()'
print(is_balanced_parentheses(text))
"""
text = "When an Open Data (standard) is created and promoted, it’s [important ]to think why - what change is th=is {trying (to] drive}? What will people do with this data that they couldn’t do before?"

ls = LStack()  # 初始化一个栈 用来存储左括号

# 先定义好验证条件
parens = "()[]{}"  # 关注字符
left_parens = "([{"  # 入栈的字符
opposite = {')':'(',']':'[','}':'{'}  # 匹配原则

# 编写生成器,用来遍历字符串,不断的提供括号及位置
def parent(text):
    # 通过开两个变量记录字符和字符位置
    i,text_len = 0,len(text)

    # 开始遍历字符串
    while True:
        while i < text_len and text[i] not in parens:
            i += 1

        # 判定因为什么结束上一个循环
        if i >= text_len:
            return
        else:
            yield i,text[i]  # 提供位置和括号字符
            i += 1

# 验证过程封装位函数
def ver():
    for i, c in parent(text):
        if c in left_parens:
            ls.push((i,c))  # 入栈一个元组
        # 遇到了右括号
        elif ls.is_empty() or ls.pop()[1] != opposite[c]:
            print("Unmatch is found at %d for %s"%(i,c))
            break
    else:
        if ls.is_empty():
            print("All parens is matched")
        else:
            # 左括号多了 (i,c)
            print("Unmatch is found at %d for %s"%ls.pop())

# if __name__ == "__main__":
#     ver()


"""
求一个数的阶乘  n!

"""
# 循环
def fun(n):
    result = 1
    for i in range(1,n + 1):
        result *= i
    return  result

# 递归
def recursion(n):
    if n <= 1:
        return 1
    return n * recursion(n - 1)

# print(recursion(5))


"""
bitree.py  二叉树的遍历实践

思路分析:
1. 使用链式结构存储二叉树的节点数据
2. 节点中存储 数据, 左孩子链接,右孩子链接 三个属性
"""
# 二叉树节点类
class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

# 二叉树遍历方法
class Bitree:
    def __init__(self,root):
        self.root = root

    # 先序遍历
    def preOrder(self,node):
        if node is None:
            return
        print(node.val)
        self.preOrder(node.left)
        self.preOrder(node.right)

    # 中序遍历
    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.val)
        self.inOrder(node.right)

    # 后序遍历
    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.val)

    #　层次遍历
    def levelOrder(self,node):
        """
        node先入队,循环判断,队列不为空时,出队表示遍历,
        同时让出队元素的左右孩子入队
        """
        sq = SQueue()
        sq.enqueue(node)
        while not sq.is_empty():
            node = sq.dequeue()
            print(node.val) # 遍历元素
            if node.left:
                sq.enqueue(node.left)
            if node.right:
                sq.enqueue(node.right)

# if __name__ == '__main__':
#     b = Node('B')
#     f = Node('F')
#     g = Node('G')
#     d = Node('D',f,g)
#     h = Node('H')
#     i = Node('I')
#     e = Node('E',h,i)
#     c = Node('C',d,e)
#     a = Node('A',b,c)  # 整个树根
#
#     bt = Bitree(a)  # 把a作为根节点进行遍历
#
#     bt.preOrder(bt.root)
#     print("========================")
#     bt.inOrder(bt.root)
#     print("========================")
#     bt.postOrder(bt.root)
#     print("========================")
#     bt.levelOrder(bt.root)


"""
sort.py  排序方法训练
冒泡排序
选择排序
插入排序
快速排序    

search.py 二分查找
"""
# 冒泡排序
def bubble_sort(l):
    n = len(l)
    # 外层循环来确定比较多少轮
    for i in range(n - 1):
        # 内存循环确定每轮两两比较多少次
        for j in range(n - 1 - i):
            if l[j] > l[j + 1]:
                l[j],l[j+1]=l[j+1],l[j]


# 选择排序
def selection_sort(list_):
    n = len(arr)
    # 遍历所有元素
    for i in range(n):
        # 找到最小元素的索引
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 交换找到的最小元素和当前元素
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# 插入排序
def insertion_sort(list_):
    # 遍历从第二个元素开始的所有元素
    for i in range(1, len(arr)):
        key = arr[i]
        # 将当前元素与已排序的部分进行比较，并找到插入位置
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# 一轮交换
def sub_sort(l,low,high):
    # 选定基准
    x = l[low]
    while low < high:
        # 后面的数向前甩
        while l[high] > x and high > low:
            high -= 1
        l[low] = l[high]  # 将比基准小的数放到前面
        # 前面的数往后甩
        while l[low] <= x and low < high:
            low += 1
        l[high] = l[low] # 将比基准大的数放到后面
    l[low] = x # 将基准数插入
    return low

# 快速排序
def quick(l,low,high):
    if low < high:
        key = sub_sort(l,low,high)
        quick(l,low,key - 1)
        quick(l,key+1,high)

# l = [4,9,3,1,2,5,8,4]
# quick(l,0,len(l)-1)
# print(l)  # 有序

# 二分查找 有序数组中查找
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # 找到目标元素，返回其索引
        elif arr[mid] < target:
            left = mid + 1  # 目标元素在右半部分
        else:
            right = mid - 1  # 目标元素在左半部分
    return -1  # 未找到目标元素

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = binary_search(arr,8)
# print(result)