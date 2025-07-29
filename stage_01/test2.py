"""
函数 function

"""

#定义函数
# def atttack01(count):  # 形式参数
#     """
#     攻击
#     :param count: 次数
#     :return:
#     """
#     for i in range(count):
#         print("直拳")
# # 调用函数
# atttack01(1)  #实际参数


# def graphics_return(count,char):
#     for r in range(count):
#         for c in range(r+1):
#             print(char, end ="")
#         print()
# graphics_return(4,"#")


# def one_dimensional_list(list_target):
#     """
#     打印一维列表
#     :param list_target: 目标列表
#     """
#     for i in list_target:
#         print(i)
# one_dimensional_list([1,2,3])


# list01 =[
#     [1,2,3,4],
#     [5,8],
#     [9,11,12],
#     [13,14,15,16,]
# ]
# def two_dimensional_list(list_target):
#     """
#     打印二维列表
#     :param list_target:  目标列表
#     """
#     for item in list_target:
#         result = " ".join(str(i) for i in item )
#         print(result)
# two_dimensional_list(list01)



# def each_unit_sum(number):
#     """
#     计算整数的每位相加和
#     :param number:四位整数
#     :return:计算的结果
#     """
#     result = number % 10
#     result += number // 10 % 10
#     result += number // 100 % 10
#     result += number // 1000
#     return result
# result = each_unit_sum(1234)
# print("四位数相加和为:" + str(result))



# def compute_weight(liang_weight):
#     """
#     根据两计算斤两
#     :param liang: 多少两
#     :return: 元组(斤,两)
#     """
#     jin = liang_weight // 16
#     liang = liang_weight % 16
#     return (jin,liang)
# jin,liang = compute_weight(65)
# print("为:" + str(jin) + "斤零" + str(liang) + "两" )



# def grade_level(score):
#     if score > 100 or score < 0:
#         return  '成绩错误'
#     if 90 <= score:
#         return  '优秀'
#     if 75 <= score:
#         return  '良好'
#     if 60 <= score:
#         return  '及格'
#     return  '不及格'
# level = grade_level(98)
# print(level)


# def judgment_value(list_name):
#     for r in range(len(list_name) - 1):
#         for c in range(r + 1, len(list_name)):
#             if list_name[r] == list_name[c]:
#                 return  True
#     return False
# print(judgment_value([3,54,2,85,10,5,78,99]))



# def is_leap_year(year):
#     return year % 4 == 0 and year % 100 != 0  or  year % 400 == 0
#
# def counting_days(year,month):
#     if month < 1 or month > 12:
#         return 0
#     if month in (4, 6, 9, 11):
#         return 30
#     if month == 2 :
#         return 29 if is_leap_year(year) else 28
#     return 31
# print(counting_days(2000,3))


# def ascending_order(numerical_list):
#     for r in range(len(numerical_list) - 1):
#         for c in range(r+1, len(numerical_list)):
#             if numerical_list[r] > numerical_list[c]:
#                 numerical_list[r],numerical_list[c] = numerical_list[c],numerical_list[r]
#     #return numerical_list 传入的可变对象，并且函数体修改的是传入的对象，则无需通过return返回结果
# list02 = [3, 54, 63, 27, 85, 2, 5, 78]
# ascending_order(list02)
# print(list02)


# list01 =[
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ]
# def policy_transposition(policy_list):
#     for c in range(1, len(policy_list)):  #方针转置
#         for r in range(c, len(policy_list)):
#             policy_list[r][c - 1],policy_list[c - 1][r] = policy_list[c - 1][r],policy_list[r][c - 1]
# policy_transposition(list01)
# print(list01)


# count = 0
# def fun01():
#     global count
#     count += 1
#
# fun01()
# fun01()
# print(count)


# def fun02(a,b,c,d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
# fun02(1,2,3,4)                #位置实参
# fun02(b=1,d=2,c=3,a=4)        #关键字实参
# list01 = ["a","b","c","d"]
# fun02(*list01)                #序列形参
# dict01 ={"a":1,"c":3,"d":3,"b":4}
# fun02(**dict01)                 #字典传参



# def fun03(a=0,b=1,c=2,d=3): #关键字实参+缺省形参，调用者可以随意传参
#     print(a)
#     print(b)
#     print(c)
#     print(d)
# fun03(b=4,c=5)


# def get_seconds(hour = 0,minutes = 0,seconds = 0):
#     return  hour * pow(60,2) + minutes * 60 +  seconds
# print(get_seconds(hour = 1,minutes = 1,seconds=2))


# def fun04(*args):  #星号将所有实参合并为一个元组 让实参个数无限制
#     print(args)
# fun04()
# fun04(1,)
# fun04(1,2)

# def adds_number(*args):
#     return  sum(args)
# print(adds_number(1,2,3,4,5,6))


# def fun05(a,*args,b): #命名关键字形参，在星号元组形参以后位置的形参，要求实参必须使用关键字形参
#     print(a)
#     print(args)
#     print(b)
# fun05(1,b=2)
# fun05(1,2,3,4,b=9)


# def fun06(**a): #双星号字典形参，实参合并为字典，实参可以传递数量无限的关键字实参
#     print(a)
# fun05(a=1,b=2)


# def fun07(a,b,*args,c,d,**kwargs):
#     print(a,b,args,c,d,kwargs)
# fun07(1,2,3,4,5,c=6,d=7,e=8,f=9)


# str01 = " 校 训：自 强不息丶厚德载物。  "
# print(str01.count(" ")) #多少次空格
# print(str01.strip()) #删除前后空格
# print(str01.replace(" ","")) #剔除所有空格
# print(str01.find("载物")) #查找字符位置
# print(str01.startswith("校训")) #判断是否字符开头


# def is_prime(num):
#     for item in range(2, num):
#         if num % item == 0:
#             return False
#     return True
#
# def judgment_prime_number(start_num,end_num):
#     prime_number_list = []
#     for num in range(start_num,end_num):
#         if is_prime(num):
#             prime_number_list.append(num)
#     return  prime_number_list
#     #return [num for num in range(start_num,end_num) if is_prime(num) ]
# print(judgment_prime_number(10,100))

