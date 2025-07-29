"""
面向对象
    类 与 对象
        类 ：抽象的概念 类别
            人
            数据(变量)成员：身高/体重
            行为(函数/方法)成员：吃饭/睡觉

        对象：具体的事物  个体
            zzl
            数据成员：170/60
            行为成员：调用

    实例方法：操作对象的变量
    类方法：操作类的变量
    静态方法：不需要操作上述两种变量

"""

# #类
# class Wife:
#     #类变量
#     total_money =1000
#     #类方法
#       #因为类方法没有对象地址self,所有不能访问实例成员
#     @classmethod
#     def print_total_money(cls):
#         print(cls.total_money)

#     #数据成员
#     def __init__(self,name,sex):
#         #self是调用当前方法的对象地址
#         self.name = name
#         self.sex = sex
#     #行为成员
#     def play(self):
#         print(self.name + "玩耍")
#
# #创建对象,实际在调用__init__方法
# w01 = Wife("AA","女") #自动将对象地址传入方法
# #调用对象的行为
# w01.play()


# class Student:
#     def __init__(self,name,age,score,sex):
#         self.name = name
#         self.age = age
#         self.score = score
#         self.sex =sex
#
#     def print_info(self):
#         print("学生%s的年龄是%d,成绩是%.2f,性别是%s" % (self.name, self.age, self.score, self.sex))

#控制台输入然后打印
# student_info =[]
# while True:
#     name = input("输入姓名:")
#     if name == "":
#         break
#     age = int(input("输入年龄:"))
#     score = float(input("输入成绩:"))
#     sex = input("输入性别:")
#     #通过形成一个字典添加到列表
#     #list01.append({"name": name, "age": age, "score": score, "sex": sex})
#     stu = Student(name,age,score,sex)
#     student_info.append(stu)
#
# for stu in student_info:
#     stu.print_info()


#定义函数查找打印
# list01 =[
#     Student("A",28,100,"女"),
#     Student("B",30,60,"男"),
#     Student("C",99,23,"女"),
#     Student("D",10,80,"男"),
#     Student("E",65,79,"女")
# ]
# def find_name():
#     for item in list01:
#         if item.name == "C":
#             return item
#     #默认返回空，省略
#     #return None
# stu = find_name()
# print(stu.name,stu.age)

# def find_sex():
#     list02=[]
#     for item in list01:
#         if item.sex == "女":
#             list02.append(item)
#     return list02
# python_re = find_sex()
# for i in python_re:
#     print(i.name,i.age)

# def find_age():
#     count = 0
#     for item in list01:
#         if item.age >=30:
#             count +=1
#     return count
# print(find_age())

# def update_score():
#     for item in list01:
#         item.score = 0
# update_score()
# for i in list01:
#     print(i.name,i.score)

# def get_name():
#     list03 = []
#     for item in list01:
#         list03.append(item.name)
#     return list03
# python_re = get_name()
# print(python_re)

# def find_max_age():
#     max_list = list01[0]
#     for item in range(1,len(list01)):
#         if list01[item].age > max_list.age:
#             max_list = list01[item]
#     return max_list
# python_re = find_max_age()
# python_re.print_info()



# class WifeCount:
#     total_count = 0
#     @classmethod
#     def pingt_count(cls):
#         print("老婆有%d个"%(cls.total_count))
#
#     def __init__(self,name):
#         self.name = name
#         WifeCount.total_count += 1
# WifeCount("sss")
# WifeCount("aaa")
# WifeCount("bbb")
# WifeCount.pingt_count()


# #二维定位
# list04 = [
#     ["00","01","02","03","04"],
#     ["10","11","12","13","14"],
#     ["20","21","22","23","24"]
# ]
# class Vector2:
#     """
#     二维向量
#     可以表示位置/方向
#     """
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     @staticmethod
#     # 静态方法:向左
#     def left():
#         return Vector2(0,-1)
#
#     @staticmethod
#     # 静态方法:向右
#     def right():
#         return Vector2(0,1)
#
#     @staticmethod
#     def up():
#         return Vector2(-1,0)
#
#     @staticmethod
#     def down():
#         return  Vector2(1,0)
#
# def get_elements(target,vect_pos,vect_dir,count):
#     """
#     再二维列表中获取指定位置方向数量的元素
#     :param target: 列表
#     :param vect_pos: 位置
#     :param vect_dir:方向
#     :param count: 个数
#     :return:    新列表
#     """
#     list05=[]
#     for i in range(count):
#         vect_pos.x += vect_dir.x
#         vect_pos.y += vect_dir.y
#         list05.append(target[vect_pos.x][vect_pos.y])
#     return list05
# python_re = get_elements(list04,Vector2(0,3),Vector2.down(),2)
# print(python_re)



# # 敌人类
# class Enemy:
#     def __init__(self,name,hp,attack,defensive):
#         self.name = name
#         self.hp = hp
#         self.attack = attack
#         self.defensive = defensive
#
#     def print_info(self):
#         print("%s的血量是%d,攻击力是%d,防御力是%d"%(self.name,self.hp,self.attack,self.defensive))
#
# enemy_list = [
#     Enemy("灭霸",100,80,50),
#     Enemy("AA",78,20,40),
#     Enemy("BB",65,42,16),
#     Enemy("CC",0,17,0),
#     Enemy("DD",0,50,0)
#     ]
# def fun01():
#     for i in enemy_list:
#         if i.name =='灭霸':
#             return i
# re01 = fun01()
# if re01:
#     re01.print_info()
# else:
#     print("空")
#
# def fun02():
#     result_list = []
#     for i in enemy_list:
#         if i.hp == 0:
#             result_list.append(i)
#     return result_list
# re02 = fun02()
# for item in re02:
#     item.print_info()
#
#
# def calculate01():
#     total_attack = 0
#     for i in enemy_list:
#         total_attack += i.attack
#     return  total_attack / len(enemy_list)
# re03 = calculate01()
# print(re03)
#
#
# def delete01():
#     for i in range(len(enemy_list)-1,-1,-1):
#         if enemy_list[i].defensive < 10:
#             del enemy_list[i]
# delete01()
#
# def addatk01():
#     for i in enemy_list:
#         i.attack += 50
# addatk01()


