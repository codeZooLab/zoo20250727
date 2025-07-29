"""

    迭代
        可迭代对象iterable
        迭代器对象iterator

"""
# # 可迭代对象  -- 容器
# list01  = [43,3,4,5,567]
# # 迭代过程
# # for item in list01:
# #     print(item)
#
# # 迭代原理
# # 面试题：for循环的原理是什么？
# #        答：1. 获取迭代器
# #           2. 循环获取下一个元素
# #           3. 遇到异常停止迭代
#
# #        可以被for的条件是什么？
# #        答：能被for的对象必须具备__iter__方法
# #        答：能被for的对象是可迭代对象
#
# #1. 获取迭代器
# iterator = list01.__iter__()
# #2. 循环获取下一个元素
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     #3. 遇到异常停止迭代
#     except StopIteration:
#         break# 退出循环
#
# # 练习1
# tuple01 = ("a","b","c")
# iterator01 = tuple01.__iter__()
# while True:
#     try:
#         print(iterator01.__next__())
#     except:
#         break
# dict01 = {"a":101,"b":102,"c":103}
# iterator02 = dict01.__iter__()
# while True:
#     try:
#         print(dict01[iterator02.__next__()])
#     except:
#         break


# # 创建迭代器
# class Skill:
#     pass
# class SkillManager:
#     """
#         技能管理器  可迭代对象
#     """
#     def __init__(self):
#         self.__skills = []
#     def add_skill(self, skill):
#         self.__skills.append(skill)
#
#     def __iter__(self):
#         # 创建一个迭代器对象,并传递需要迭代的数据。
#         return SkillIterator(self.__skills)
# class SkillIterator:
#     """
#         技能迭代器
#     """
#     def __init__(self, target):
#         self.__target = target
#         self.__index = 0
#
#     def __next__(self):
#         # 如果没有数据了，则抛出异常
#         if self.__index > len(self.__target) - 1:
#             raise StopIteration
#         # 返回下一个数据
#         temp = self.__target[self.__index]
#         self.__index += 1
#         return temp
#
# manager = SkillManager()
# manager.add_skill(Skill())
# manager.add_skill(Skill())
# manager.add_skill(Skill())
#
# # for item in manager:
# #     print(item)
#
# iterator = manager.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break

# # 练习图像管理器
# class Graphic:
#     pass
# class GraphicManager:
#     def __init__(self):
#         self.__graphics = []
#
#     def add_manage(self,graphic_item):
#         self.__graphics.append(graphic_item)
#
#     def __iter__(self):
#         return GraphicIterator(self.__graphics)
#
# class GraphicIterator:
#     def __init__(self,target):
#         self.__target = target
#         self.index = 0
#
#     def __next__(self):
#         if self.index == len(self.__target):
#             raise StopIteration
#         item = self.__target[self.index]
#         self.index += 1
#         return item
#
# graphic = GraphicManager()
# graphic.add_manage(Graphic())
# graphic.add_manage(Graphic())
# graphic.add_manage(Graphic())
# iterator = graphic.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break


# # 练习myrang类
# class MyRang:
#     def __init__(self,end_num):
#         self.end_num = end_num
#
#     def __iter__(self):
#         return MyRangIterator(self.end_num)
# class MyRangIterator:
#     def __init__(self,end_num):
#         self.__end_num = end_num
#         self.__index = 0
#
#     def __next__(self):
#         if self.__index == self.__end_num:
#             raise StopIteration
#         temp = self.__index
#         self.__index += 1
#         return temp
#
# for item in MyRang(8):
#     print(item)
# # r01 =  MyRang(8)
# # iterator = r01.__iter__()
# # while True:
# #     try:
# #         print(iterator.__next__())
# #     except StopIteration:
# #         break


"""

   迭代器 --> yield

"""
# class MyRange:
#     def __init__(self, stop_value):
#         self.stop_value = stop_value
#
#     def __iter__(self):
#         # return MyRangeIterator(self.stop_value)
#         # 0 --> self.stop_value
#         # yield 作用: 将下列代码改为迭代器模式的代码.
#         # 生成迭代器代码的大致规则:
#         # 1. 将yield以前的语句定义在next方法中
#         # 2. 将yield后面的数据作为next方法返回值
#         number = 0
#         while number < self.stop_value:
#             yield number
#             number += 1
#
# # next一次，计算一次，返回一次。
# # for item in MyRange(10):
# #     print(item)
# my01 = MyRange(10)
# iterator = my01.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break


# # 练习图像管理器 --> yieid
# class Graphic:
#     pass
# class GraphicManager:
#     def __init__(self):
#         self.__graphics = []
#
#     def add_manage(self,graphic_item):
#         self.__graphics.append(graphic_item)
#
#     def __iter__(self):
#         index = 0
#         while index < len(self.__graphics):
#             yield self.__graphics[index]
#             index += 1
#
# graphic = GraphicManager()
# graphic.add_manage(Graphic())
# graphic.add_manage(Graphic())
# graphic.add_manage(Graphic())
# iterator = graphic.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break


"""
    yield --> 生成器
"""
"""
# 生成器原理
class MyGenerator:
    # 生成器 = 可迭代对象 + 迭代器
    def __init__(self,stop_value):
        self.begin = 0
        self.stop_value = stop_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.begin >= self.stop_value:
            raise StopIteration
        temp = self.begin
        self.begin+=1
        return temp
"""
# def my_range(stop_value):
#     number = 0
#     while number < stop_value:
#         yield number
#         number += 1
# my01 = my_range(10)
# print(type(my01), dir(my01))  # dir 获取对象所有成员
# for item in my01:
#     print(item)

# # 练习1
# list01 = [4,5,77,54,23,86]
# def get_even():
#     for item in list01:
#         if item % 2 == 0:
#             yield item
# g01 = get_even()
# for item in g01:
#     print(item)


"""
    内置生成器
        枚举函数enumerate：遍历可迭代对象时，可以将索引与元素组合为一个元组
        zip：将多个可迭代对象中对应的元素组合成一个个元组，生成的元组个数由最小的可迭代对象决定
"""
# list02 = [4,5,77,54,23,86]
# for index,elemment in enumerate(list02):
#     print(index,elemment)
# # 练习2
# def my_enumerate(iterable_target):
#     index = 0
#     for enumerate in iterable_target:
#         yield (index,enumerate)
#         index += 1
# for item in my_enumerate(list02):
#     print(item)


# list03 = ["A","B","C","D"]
# list04 = [101,102,103,104,105]
# for item in zip(list03,list04):  # zip 返回多个对象相同索引合并后的元组
#     print(item)
# 练习3
# def my_zip(*args):
#     for index in range(len(min(args,key=lambda item:len(item)))):
#         result_list = []
#         for item in args:
#             result_list.append(item[index])
#         yield tuple(result_list)
# for item in my_zip(list03,list04):
#     print(item)


"""
    生成器表达式
        1.	定义：用推导式形式创建生成器对象。
        2.	语法：变量 = ( 表达式 for 变量 in 可迭代对象 [if 真值表达式] )
"""
# list01 = [3, "54", True, 6, "76", 1.6, False, 3.5]
# # 生成器函数
# def find01():
#     for item in list01:
#         if type(item) == int:
#             yield item + 1
# python_re = find01()
# for item in python_re:
#     print(item)
#
# #  生成器表达式
# # 此时没有计算,更没有结果
# python_re = (item + 1 for item in list01 if type(item) == int)
# # 一次循环,一次计算,一个结果
# for item in python_re:
#     print(item)
#
# # 列表推导式
# # 此时已经完成所有计算,得到所有结果
# python_re = [item + 1 for item in list01 if type(item) == int]
# # 只是获取所有结果
# for item in python_re:
#     print(item)
#
# # 变量 = [itme for item in 可迭代对象 if 条件] 列表推导
# # 变量 = {k,v for k,v in 可迭代对象 if 条件} 字典推导
# # 变量 = {item for item in 可迭代对象 if条件} 集合推导
# # 变量 = (item for item in 可迭代对象 if条件) 生成器表达式
#
#
# # 练习
# # 生成器函数
# def find02():
#     for item in list01:
#         if type(item) == float:
#             yield item
# for item in find02():
#     print(item)
# # 生成器表达式
# for item in (item for item in list01 if type(item) == float):
#     print(item)
#
#
# # 练习
# class SkillData:
#     def __init__(self,id,name,atk_ratio,duration):
#         self.id = id
#         self.name = name
#         self.atk_ratio = atk_ratio
#         self.duration = duration
#
#     def __str__(self):
#         return "技能数据是:%d,%s,%d,%d"%(self.id,self.name,self.atk_ratio,self.duration)
#
# list_skill = [
#     SkillData(101,"乾坤大挪移",5,10),
#     SkillData(102,"降龙十八掌",8,5),
#     SkillData(103,"葵花宝典",10,2),
# ]
# def find03():
#     for item in list_skill:
#         if item.atk_ratio > 6:
#             yield item
# for item in find03():
#     print(item)
# for item in (item for item in list_skill if item.atk_ratio > 6 ):
#     print(item)


