"""
    模块
        1.定义:包含一系列数据、函数、类的.py文件
        2.作用:让一些相关的数据，函数，类有逻辑的组织在一起，使逻辑结构更加清晰。有利于多人合作开发。

    模块变量
        1.__all__ 定义当前模块可导出成员，仅对from xx import *语句有效
            __all__ = ["fun","class"]
        2.__doc__ 查看文档注释
        3.__file__ 返回当前文件的绝对路径
        4.__name__ 返回文件名称，主模块__main__ 非主模块为真名
            用做判断if __name__ == '__main__'(不是主模块则不执行，是主模块则执行)

    分类
        1.内置模块(builtins)，在解析器的内部可以直接使用。
        2.标准库模块，安装Python时已安装且可直接使用。
        3.第三方模块（通常为开源），需要自己安装。
        4.用户自己编写的模块（可以作为其他人的第三方模块）

"""
import sys

# 导入模块方式1
# 本质:使用变量名inheritance_polymorphism关联模块地址
#import inheritance_polymorphism as i01
# v01 = i01.Vector1(10)
# v02 = v01 + 2
# print(v02)

# 导入模块方式2
# 本质: 将指定的成员导入到当前模块作用域中
# 小心: 导入进来的成员与当前模块成员名称相同
# from inheritance_polymorphism import Vector1
# v01 = Vector1(20)
# v02 = 2 * v01
# print(v02)

# 导入模块方式3
# 本质: 将指定模块的所有成员导入到当前模块作用域中
# 小心: 导入进来的成员与其他模块成员冲突
# 针对import *,单下划线_开头的为隐藏成员，不会被导入
# from inheritance_polymorphism import *
# v01 = Vector1(20)
# v01 -= 2
# print(v01)


"""
    时间处理
"""
import time

# print(time.time()) # 获取当前时间戳 1970.1.1至今秒数
# print(time.localtime()) # 时间元组 年月日时间秒 周天 年天 夏令时
# # 通过元组获取时间
# # 时间戳 --> 时间元组
# tuple_time = time.localtime()
# for item in tuple_time:
#     print(item)
# print(tuple_time[1])
# # 通过类获取时间
# print(tuple_time.tm_year)
# # 时间元组 --> 时间戳
# print(time.mktime(tuple_time))
# # 时间元组 --> str
# str_time =  time.strftime("%Y/%m/%d %H:%M:%S",tuple_time)
# print(str_time)
# # str --> 时间元组
# print(time.strptime(str_time,"%Y/%m/%d %H:%M:%S"))
#
# # 计算星期几
# def get_week(year,month,day):
#      tuple_time = time.strptime("%d/%d/%d"%(year,month,day),"%Y/%m/%d")
#      dict_weeks = {
#          0:"星期一",
#          1:"星期二",
#          2:"星期三",
#          3:"星期四",
#          4:"星期五",
#          5:"星期六",
#          6:"星期日"
#      }
#      return dict_weeks[tuple_time[6]]
# print(get_week(2025,5,12))

# # 计算活多少天
# def life_day(year,month,day):
#     tuple_time = time.strptime("%d/%d/%d" % (year, month, day), "%Y/%m/%d")
#     life_second = time.time() - time.mktime(tuple_time)
#     return int(life_second // (3600 * 24))
# print(life_day(2000,10,23))


"""
    异常处理：将程序由异常状态转为正常流程
"""
# def fun01(count):
#     preson = int(input("人数:"))
#     result = count / preson
#     print("结果为%d"%(result))
# try:
#     # 可能出错的代码
#     fun01(10)
# except ValueError:
#     print("人数必须为整数")
# except ZeroDivisionError:
#     print("人数不能为O")
# except Exception:  # 异常基类
#     print("未知错误")
# else:
#     # 如果异常，则不执行语句
#     print("未出错")
# finally:
#     # 无论是否异常，一定执行的代码
#     print("finally")
# print("aaa")


# # 练习
# def funo2():
#     while True:
#         str_score = input("成绩:")
#         try:
#             int_score = float(str_score)
#         except:
#             print("转换错误")
#             continue
#         else:
#             if 0 <= int_score <= 100:
#                 print("正常数值")
#                 return int_score
#             else:
#                 print("非正常数值")
#                 continue
# print(funo2())


"""
    raise语句：抛出一个错误，让程序进入异常状态
    自定义异常类：封装错误信息
"""
# class AgeError(Exception):
#     def __init__(self,message,age_value,code_line,error_number):
#         super().__init__("出错了")
#         self.message = message
#         self.age_value = age_value
#         self.code_line = code_line
#         self.error_number = error_number
#
# class Wife:
#     def __init__(self,age):
#         self.age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self,value):
#         if 21 <= value <= 31:
#             self.__age = value
#         else:
#             # raise ValueError("我不要")
#             raise AgeError("超过想要的范围",value,164,1001)
# # w01 = Wife(81)
# try:
#     w01 = Wife(81)
# except AgeError as e:
#     print(e.message)


# # 练习
# class AtkError(Exception):
#     def __init__(self,message,code_line,atk):
#         super().__init__("异常")
#         self.message = message
#         self.code_line = code_line
#         self.atk = atk
#
# class Enemy:
#     def __init__(self,atk):
#         self.atk = atk
#
#     @property
#     def atk(self):
#         return self.__atk
#
#     @atk.setter
#     def atk(self,value):
#         if 0 <= value <= 100:
#             self.__atk = value
#         else:
#             raise AtkError("攻击力不符合范围",191,value)
# try:
#     Enemy(101)
# except AtkError as a :
#     print(a.code_line)
#     print(a.message)


