"""
    函数式编程
        1. 定义：用一系列函数解决问题。
            -- 函数可以赋值给变量，赋值后变量绑定函数。
            -- 允许将函数作为参数传入另一个函数。
            -- 允许函数返回一个函数。
	    2. 高阶函数：将函数作为参数或返回值的函数。

"""
from common.list_helper import *

# def fun01():
#     print("fun01执行喽")
#
# # 调用方法,执行方法体
# re1 = fun01()
# print(re1)
#
# # 将函数赋值给变量
# re2 = fun01
# # 通过变量,调用函数
# re2()
#
# def fun02():
#     print("fun02执行喽")
#
# # 将函数作为函数的参数进行传递
# # 将一个函数的代码(fun02/fun01),注入到另外一个函数中(fun03).
# def fun03(func):
#     print("fun03执行喽")
#     func()
# fun03(fun01)
# fun03(fun02)



"""
    函数式编程 思想
"""
class SkillData:
    def __init__(self,id,name,atk_ratio,duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

    def __str__(self):
        return "技能数据是:%d,%s,%d,%d"%(self.id,self.name,self.atk_ratio,self.duration)

list_skill = [
    SkillData(101,"乾坤大挪移",5,10),
    SkillData(102,"降龙十八掌",8,5),
    SkillData(103,"葵花宝典",10,2),
]

# """
# # 需求1:获取攻击比例大于6的所有技能
# def find01():
#     for item in list_skill:
#         if item.atk_ratio > 6:
#             yield item
#
# # 需求2:获取持续时间在4--11之间的所有技能
# def find02():
#     for item in list_skill:
#         if 4<item.duration<11:
#             yield item
#
# # 需求3:获取技能名称大于4个字并且持续时间小于6的所有技能
# def find04():
#     for item in list_skill:
#         if len(item.name) > 4 and item.duration < 6:
#             yield item
# """
# # "封装"(分而治之 变则疏之)
# # 将每个变化的条件,单独定义在函数中.
# def condition01(item):
#     return item.atk_ratio > 6
#
# def condition02(item):
#     return 4<item.duration<11
#
# def condition03(item):
#     return len(item.name) > 4 and item.duration < 6
# #
# # "继承"(隔离变化)
# def find(func_condition):
#     """
#         通用的查找方法
#     :param func_condition: 查找条件,函数类型.
#             函数名(变量) --> 返回值bool类型
#     :return:
#     """
#     for item in list_skill:
#         # "多态":调用父(变量),执行子(具体函数).
#         #       不同子类重写父类方法,执行逻辑不同.
#
#         # if item.atk_ratio > 6:
#         # if condition01(item):
#         if func_condition(item):
#             yield item
#
# for item in find(condition01):
#     print(item)
#
#
# # 测试调用通用模块list_helper实现 将find方法定义到通用模块中
# l01 = ListHelper.find_all(list_skill,condition01)
# for item in l01:
#     print(item)
# l02 = ListHelper.find_all(list_skill,lambda item:item.atk_ratio > 6) # 使用lambda实现
# for item in l02:
#     print(item)
# # 练习 lambda
# print(ListHelper.get_count(list_skill,lambda item:len(item.name) > 4))

# # 练习
# list01 = [5,10,23,45,61,100,7]
# for i in (item for item in list01 if item % 2 == 0):
#     print(i)
# for i in (item for item in list01 if item > 15):
#     print(i)
# for i in (item for item in list01 if 30 < item < 70):
#     print(i)
#
# # "封装"
# def condition04(item):
#     return item % 2 == 0
# def condition05(item):
#     return item > 15
# def condition06(item):
#     return 30 < item < 70
# # "继承"
# def find_func(condition):
#     for item in list01:
#         # "多态"
#         if condition(item) :
#             yield item
# for i in find_func(condition04):
#     print(i)


"""
    lambda匿名函数
        1.	定义：是一种匿名方法。
        2.	作用：作为参数传递时语法简洁，优雅，代码可读性强。随时创建和销毁，减少程序耦合度。
        3.	语法
            -- 定义：
                变量 = lambda 形参: 方法体
	        -- 调用：
			    变量(实参)
        4.	说明：
        -- 形参没有可以不填
        -- 方法体只能有一条语句，且不支持赋值语句。
        注意:函数体自带return
"""
# list02 = [5,10,23,45,61,100,7]
# def condition04(item):
#     return item % 2 == 0
# for i in ListHelper.find_all(list02,condition04):
#     print(i)
# lambda表达式 lambda 形参: 方法体
# for i in ListHelper.find_all(list02,lambda item:item % 2 == 0):
#     print(i)

# 练习 敌人类
class Enemy:
    def __init__(self,name,hp,attack,defensive):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defensive = defensive

    def __str__(self):
        return ("%s的血量是%d,攻击力是%d,防御力是%d"%(self.name,self.hp,self.attack,self.defensive))

enemy_list = [
    Enemy("灭霸",50,80,50),
    Enemy("成昆",78,20,40),
    Enemy("BB",65,42,16),
    Enemy("CC",0,17,0),
    Enemy("DD",90,50,75)
    ]
#
# print(ListHelper.find_single(enemy_list,lambda item:item.name == '灭霸'))
# e01 = ListHelper.find_all(enemy_list,lambda item:item.attack > 20)
# for i in e01:
#     print(i)
# """
#     # 生成器--> 惰性操作
#     # 优势：节省内存
#     # 缺点：获取结果不灵活(不能使用索引／切片访问结果)
#     # 解决：惰性操作　--> 立即操作
#     list_result = list(e01)
#     for item in list_result[:2]:
#         print(item)
# """
# print(ListHelper.get_count(enemy_list,lambda item:item.hp > 0))
# print(ListHelper.is_exists(enemy_list,lambda item:item.name == '成昆'))
# print(ListHelper.sum_total(enemy_list, lambda item:item.attack))
# for item in ListHelper.select_handle(enemy_list, lambda item:(item.name, item.hp)):
#     print(item)
# print(ListHelper.select_max(enemy_list,lambda item:item.defensive))
# ListHelper.orderby_asc(enemy_list,lambda item:item.hp)
# for item in enemy_list:
#     print(item)
# print(ListHelper.select_min(enemy_list,lambda item:item.defensive))
# ListHelper.orderby_desc(enemy_list,lambda item:item.attack)
# for item in enemy_list:
#     print(item)
# ListHelper.delete_all(enemy_list, lambda item: item.defensive > 20)
# for i in enemy_list:
#     print(i)


"""
    内置高阶函数
        1.	map（函数，可迭代对象）：使用可迭代对象中的每个元素调用函数，将返回值作为新可迭代对象元素；返回值为新可迭代对象。
        2.	filter(函数，可迭代对象)：根据条件筛选可迭代对象中的元素，返回值为新可迭代对象。
        3.	sorted(可迭代对象，key = 函数,reverse = bool值)：排序，返回值为排序结果。
        4.	max(可迭代对象，key = 函数)：根据函数获取可迭代对象的最大值。
        5.	min(可迭代对象，key = 函数)：根据函数获取可迭代对象的最小值。
"""
# # filter 根据条件筛选返回对象
# for i in filter(lambda item:item.hp == 0,enemy_list):
#     print(i)
# # map 返回对象的某一种数据
# for i in map(lambda item:item.name,enemy_list):
#     print(i)
# # max min 获取最大/最小值
# print(max(enemy_list,key = lambda item:item.hp))
# # sorted 排序 返回值为新列表 使用时需要获取结果
# # reverse 控制升序降序 默认False升序
# python_re = sorted(enemy_list,key=lambda item:item.attack,reverse=True)
# for i in python_re:
#     print(i)


# 练习
# tuple01 = ([1,1,1],[2,2],[3,3,3,3])
# print(max(tuple01,key=lambda item:len(item)))
# for i in map(lambda item:(item.name,item.attack,item.hp),enemy_list):
#     print(i)
# for i in filter(lambda item:item.attack > 50 and item.hp > 0,enemy_list):
#     print(i)
# for i in (sorted(enemy_list,key=lambda item:item.defensive,reverse=True)):
#     print(i)


"""
    外部嵌套作用域
"""
# def fun01():
#     # 是fun01函数的局部作用域
#     # 也是fun02函数的外部嵌套作用域
#     a = 1
#
#     def fun02():
#         b = 2
#         # 可以访问外部嵌套作用域变量
#         # print(a)
#         # 不能修改外部嵌套作用域变量
#         # a = 2# 创建了fun02的局部变量
#         # print(a)# 2
#
#         nonlocal a # 声明外部嵌套作用域
#         a = 2
#         print(a) # 2
#     fun02()
#     print(a) # 1
# fun01()


"""
    闭包
        1.	三要素：
            1.必须有一个内嵌函数。2.内嵌函数必须引用外部函数中变量。3.外部函数返回值必须是内嵌函数。
        2.	语法
            -- 定义：
            def 外部函数名(参数):
                    外部变量
                    def 内部函数名(参数):
                        使用外部变量
                    return 内部函数名
            -- 调用：
                   变量 = 外部函数名(参数)
                   变量(参数)
        3.	定义：在一个函数内部的函数,同时内部函数又引用了外部函数的变量。
        4.	本质：闭包是将内部函数和外部函数的执行环境绑定在一起的对象。
        5.	优点：内部函数可以使用外部变量。 
        6.	缺点：外部变量一直存在于内存中，不会在调用结束后释放，占用内存。
        7.	作用：实现python装饰器。
"""
# def fun01():
#     a = 1
#     def fun02():
#         print(a)
#     return fun02
# # 调用外部函数，返回值是内嵌函数
# result = fun01()
# # 调用内嵌函数
# result()  # 可以访问外部变量a
#
#
# # 闭包应用:逻辑连续，当内部函数被调用时，不脱离当前的逻辑
# # 压岁钱
# def give_gife_money(money):
#     """
#         得到压岁钱
#     """
#     print("得到了%d压岁钱" % money)
#
#     def child_buy(target, price):
#         """
#             孩子购买商品
#         :param target: 需要购买的商品
#         :param price: 商品单价
#         """
#         nonlocal money
#         if money >= price:
#             money -= price
#             print("孩子花了%.1f钱，购买了%s" % (price, target))
#         else:
#             print("钱不够啦")
#
#     return child_buy
# # 下列代码是一个连续的逻辑
# action = give_gife_money(10000)
# action("唐僧肉", 0.5)
# action("小汽车", 2000)
# action("手机", 8000)




