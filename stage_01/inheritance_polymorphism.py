"""
    继承 -- 方法
        方法子类不用写,但是可以用
"""
# 多个子类在概念上一致的,所以就抽象出一个父类
# 多个子类的共性,可以提取到父类中
#在实际开发中:
#从设计角度讲:先有子,在有父
#从编码角度讲:先有父亲,在有子
# class Person:
#     def say(self):
#         print("说话")
#
# class Student(Person):
#     def study(self):
#         print("学习")
#
# class Teacher(Person):
#     def teach(self):
#         print("讲课")
#
# s01 =Student()
# # 子类对象可ui调用子类成员,也可以调用父类成员
# s01.study()
# s01.say() #父类成员
#
# # 父类对象只可以调用父类成员,不可以调用子类成员
# p01 = Person()
# p01.say()
#
# t01 =Teacher()
# t01.teach()
# # python 内置函数
# # 判断对象是否属于一个类型
# print(isinstance(t01,Teacher)) # True 对象 类型
# print(isinstance(t01,Student)) # False
# print(isinstance(t01,Person)) # True
#
# # 判断一个类型是否属于另一个类型
# # "老师类型" 是不是一个学生类型
# print(issubclass(Teacher,Student)) # False 类型 类型
# print(issubclass(Teacher,Person)) # True

"""
     继承 -- 变量
"""
# class Person:
#     def __init__(self,name):
#         self.name = name
# """
# class Student(Person):
#     # 子类若没有构造函数,使用父类的
#     pass
# s01 = Student()
# print(s01.name)
# """
#
# class Student(Person):
#     # 子类若具有构造函数,则必须先调用父类构造函数
#     def __init__(self,name,score):
#         super().__init__(name)
#         self.score = score
# s01 = Student("张三",100)
# print(s01.score)
# print(s01.name)

# 练习
# class Car:
#     def __init__(self,brand,speed):
#         self.brand = brand
#         self.speed = speed

# class ElectroCar(Car):
#     def __init__(self,brand,speed,battery_capacity,charging_power):
#         super().__init__(brand,speed)
#         self.battery_capacity = battery_capacity
#         self.charging_power = charging_power
#
# c01 = Car("宝马",100)
# print(c01.brand)
# e01 = ElectroCar("比亚迪",120,15000,200)
# print(e01.brand)


"""
    继承 -- 设计
"""
# class Vehicle:
#     """
#         交通工具，代表所有具体的交通工具（火车/飞机...）
#         继承：隔离子类变化，将子类的共性提取到父类中
#     """
#     def transport(self,str_position):
#        # 因为父类太过抽象，所以写不出方法体
#         pass
#
# # 客户端代码，用交通工具
# class Person:
#     def __init__(self,name):
#         self.name = name
#
#     def go_to(self,vehicle,str_position):
#         # 多态：调用父，执行子
#         # 调用的是交通工具的运输方法
#         # 执行的是飞机的运输方法或者汽车的运输方法
#         vehicle.transport(str_position)
#
# class Car(Vehicle):
#     def transport(self,str_position):
#         print("汽车开到",str_position)
#
# class Airplane(Vehicle):
#     def transport(self,str_position):
#         print("飞机飞到",str_position)
#
# p01 = Person("老张")
# c01 = Car()
# a01 = Airplane()
# p01.go_to(c01,"东北")
# p01.go_to(a01,"东北")



# # 练习手雷爆炸
# class HandGrenade:
#     def __init__(self,atk):
#         self.atk = atk
#
#     def explosion(self,damage_target):
#         # 通过isinstance判断传入的对象是否属于父类，是则执行
#         if isinstance(damage_target,Damageable):
#             print("爆炸")
#             # 调用父类代表（玩家/敌人）的可以受伤者
#             # 执行子类（具体玩家/敌人）
#             damage_target.damage(self.atk)
#
# class Damageable:
#     """
#     可以受伤
#     继承：统一多个子类的概念，隔离变化
#     """
#     def damage(self,value):
#         # 当调用时如果子类没有damage方法，则会执行父类方法
#         # 如果子类不重写则异常
#         raise NotImplementedError
#
# class Enemy(Damageable):
#     def __init__(self,hp):
#         self.hp = hp
#
#     def damage(self,value):
#         self.hp -= value
#         print("敌人受伤")
#
# class Player(Damageable):
#     def __init__(self,hp):
#         self.hp = hp
#
#     def damage(self,value):
#         self.hp -= value
#         print("玩家受伤")
#
# g01 = HandGrenade(20)
# e01 = Enemy(50)
# p01 = Player(60)
# g01.explosion(e01)
# g01.explosion(p01)



# # 练习图像管理器
# class GraphicManager:
#     def __init__(self):
#         self.__graphics = []
#
#     def add_manage(self,graphic_item):
#         # 判断传入的是否图形
#         if isinstance(graphic_item,Graphic):
#             self.__graphics.append(graphic_item)
#         else:
#             raise ValueError("不是图形类")
#
#     def calculation_item(self):
#         total_area = 0
#         for item in self.__graphics:
#             total_area += item.calculation_area()
#         return total_area
# class Graphic:
#     def calculation_area(self):
#         raise NotImplementedError
#
# class Circle(Graphic):
#     def __init__(self,radius):
#         self.radius = radius
#
#     def calculation_area(self):
#         return 3.14 * self.radius ** 2
#
# class Rectangle(Graphic):
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#
#     def calculation_area(self):
#         return self.length * self.width
#
# c01 = Circle(5)
# r01 = Rectangle(10,20)
# g01 = GraphicManager()
# g01.add_manage(c01)
# g01.add_manage(r01)
# total = g01.calculation_item()
# print(total)


# # 练习 员工管理器
# class EmployeeManage:
#     def __init__(self):
#         self.__employees = []
#
#     def add_employee(self,employee_item):
#         if isinstance(employee_item,Employee):
#             self.__employees.append(employee_item)
#         else:
#             raise ValueError("不是员工工资类")
#
#     def calculation_item(self):
#         total_salary = 0
#         for item in self.__employees:
#             total_salary += item.calculation_salary()
#         return total_salary
#
# class Employee:
#     def __init__(self,basic_salary):
#         self.basic_salary = basic_salary
#     def calculation_salary(self):
#         return self.basic_salary
#         # raise NotImplementedError
#
# class Programmer(Employee):
#     def __init__(self,basic_salary,project_funds):
#         super().__init__(basic_salary)
#         self.project_funds = project_funds
#
#     def calculation_salary(self):
#         # return self.basic_salary + self.project_funds
#         # 扩展重写
#         return super().calculation_salary() + self.project_funds
#
# class Sales(Employee):
#     def __init__(self,basic_salary,sales_volume):
#         super().__init__(basic_salary)
#         self.sales_volume = sales_volume
#
#     def calculation_salary(self):
#         return self.basic_salary + self.sales_volume * 0.05
#
# p01 = Programmer(4000,4000)
# s01 = Sales(3000,10000)
# e01 = EmployeeManage()
# e01.add_employee(p01)
# e01.add_employee(s01)
# total = e01.calculation_item()
# print(total)


# # 内置可重写函数
# class StudentModel:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     # 对象 --> 字符串 (随意格式)
#     def __str__(self):
#         return "我叫%s,年龄是%d"%(self.name,self.age)
#
#     # 对象 --> 字符串 (解释器可识别,有格式)
#     def __repr__(self):
#         return "StudentModel('%s',%d)"%(self.name,self.age)
#
# s01 = StudentModel("zs",20)
# str01 = str(s01) # 原本返回对象地址,通过重写str函数 转换为特定格式的字符串
# print(str01)
# str02 = repr(s01)
# print(str02)
# # python_re = eval("1+2*5") # eval根据字符串执行python代码 还有exec等
# # print(python_re)
#
# # 克隆对象
# # 通过repr 返回python格式的字符串（实际返回上面创建对象的代码）
# # eval 根据返回的字符串执行代码
# s02 = eval(repr(s01))
# s02.name = "ls"
# print(s01.name,s02.name)


# 运算符重载 反向重载 复合重载
class Vector1:
    def __init__(self,x):
        self.x = x

    def __str__(self):
        return str(self.x)
    # 重载
    def __add__(self, other):
        return Vector1(self.x + other)
    # 反向重载
    def __rmul__(self, other):
        return Vector1(self.x * other)
    # 复合重载
    def __isub__(self, other):
        self.x -= other
        return self

v01 = Vector1(10)
# 重写
v02 = v01 + 2
print(str(v02))
# 反向重写
v03 = 2 * v01
print(str(v03))
# 复合重写__isub__,实现在原对象基础上的变化
# 如果不重写__isub__,默认使用__sub__,一般会产生新对象
v01 -= 2
print(str(v01))