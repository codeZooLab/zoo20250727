"""
    封装
    封装数据:
        敌人(姓名/血量/攻击力/防御力)
        优势:更符合人类思考方式
            将数据与对数据的操作整合在一起
    封装行为:
        二维列表助手类(获取多个元素) 向量(向左/向右/求方向)
        优势:以模块化的方式进行编程
            可以集中精力设计/组织多个类协同工作
"""
# #使用方法封装变量
# class Wife:
#     # __slots__ = ("__name","__age") #限制一个类创建的实例只能有固定实例变量
#     def __init__(self,name,age):
#         self.name = name
#         # 本质:障眼法(实际将变量名改为:_类名__age)
#         #self.__age = age
#         #通过调用类方法
#         self.set_age(age)
#
#
#     #提供公开的读写方法
#     def get_age(self):
#         return self.__age
#
#     def set_age(self,value):
#         if 21 <= value <40:
#             self.__age = value
#         else:
#             raise ValueError("我不要")
#
# """
# w01 = Wife("aa",50)
# # w01.__age = 80 #重新创建了新的实例变量(没有改变类中定义的__age)
# #w01._Wife__age = 100 #修改了类中定义的私有变量
# print(w01.get_age())
# #print(w01.__dict__)  #python内置变量,存储对象的实例变量
# """
# w01 = Wife("aa",30)
# w01.set_age(21)
# print(w01.get_age())


# #使用property(读取方法,写入方法)封装变量
# class Wife:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age  #self.age是类变量
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self,value):
#         if 21 <= value <40:
#             self.__age = value   #__age实际实现的效果是区别类变量age，并且私有化该变量，如果写其他变量名也能成功
#         else:
#             raise ValueError("我不要")
#     #属性 property对象拦截对age类变量的读写操作
#     age = property(get_age,set_age)
#
# w01 = Wife("aa",30)
# w01.age = 25
# print(w01.age)
# print(w01.__dict__)


# #使用属性property,封装变量
# class Wife:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     @property #创建property对象，只负责拦截读取操作
#     def age(self):
#         return self.__age
#     @age.setter #只负责拦截写入操作
#     def age(self,value):
#         if 21 <= value <40:
#             self.__age = value
#         else:
#             raise ValueError("我不要")
#
# w01 = Wife("aa",30)
# w01.age = 25
# print(w01.age)
# print(w01.__dict__)



#使用方法封装
# class Enemy:
#     def __init__(self,name,hp,attack):
#         self.name = name
#         #self.hp = hp
#         self.set_hp(hp)
#         self.attack = attack
#
#     def get_hp(self):
#         return self.hp
#
#     def set_hp(self,value):
#         if 10 <= value <=50:
#             self.hp = value
#         else:
#             raise ValueError("不行")
#
# w02 = Enemy("aa",50,30)
# w02.set_hp(15)
# print(w02.get_hp())
# #print(w02.__dict__)


# #使用property
# class Enemy:
#     def __init__(self,name,hp,attack):
#         self.name = name
#         self.hp = hp
#         self.attack = attack
#
#     def get_hp(self):
#         return self.__hp
#
#     def set_hp(self,value):
#         if 10 <= value <=50:
#             self.__hp = value
#         else:
#             raise ValueError("不行")
#
#     hp = property(get_hp,set_hp)
#     #hp = property(None,set_hp) 只读
#
# w02 = Enemy("aa",50,30)
# w02.hp = 21
# print(w02.hp)
# print(w02.__dict__)


# #使用属性property
# class Enemy:
#     def __init__(self,name,hp,attack):
#         self.name = name
#         self.hp = hp
#         self.attack = attack
#     @property
#     def hp(self):
#         return self.__hp
#     @hp.setter
#     def hp(self,value):
#         if 10 <= value <=50:
#             self.__hp = value
#         else:
#             raise ValueError("不行")
#
# w02 = Enemy("aa",50,30)
# w02.hp = 10
# print(w02.hp)
# print(w02.__dict__)


# # 小明在招商银行取钱
# class Preson:
#         def __init__(self,name,money):
#             self.name = name
#             self.money = money
#         @property
#         def name(self):
#             return self.__name
#         @name.setter
#         def name(self,value):
#             self.__name = value
#         @property
#         def money(self):
#             return self.__money
#         @money.setter
#         def money(self, value):
#             self.__money = value
# class Bank:
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, value):
#         self.__name = value
#     @property
#     def money(self):
#         return self.__money
#     @money.setter
#     def money(self, value):
#         self.__money = value
#
#     def draw_money(self,preson,value):
#         self.money -= value
#         preson.money += value
#         print("%s在%s取%d块钱"%(preson.name,self.__name,value))
#         print(preson.money,self.__money)
# xm = Preson("小明",0)
# bak = Bank("招商银行",500000000)
# bak.draw_money(xm,5000)


# #练习1 对象区分数据的不同
# class Person:
#     def __init__(self,name,money,skill):
#         self.name = name
#         self.money = money
#         self.skill = skill
#
#     def teach(self,who):
#         print(self.name,"教",who.name,self.skill)
#
#     def work(self,value):
#         self.money += value
#         print("%s上班挣了%.2f元"%(self.name,value))
#
# per01 = Person("张无忌",500,"九阳神功")
# per02 = Person("赵敏",0,"化妆")
# per01.teach(per02)
# per02.work(2000)



# #练习2 类与类间的方法调用  类区分行为的不同
# class Player:
#     def __init__(self,name,hp,ack):
#         """
#         人物
#         :param name: 名称
#         :param hp: 血量
#         :param ack:攻击力
#         """
#         self.name = name
#         self.hp = hp
#         self.ack = ack
#
#     def attack(self,other):
#         #攻击的逻辑
#         print(self.name,"攻击",other.name)
#         #通过被攻击对象的地址调用受伤方法
#         other.damage(self.ack)
#
#     def damage(self, value):
#         #受伤的逻辑
#         print(self.name,"被攻击,受伤掉血")
#         self.hp -= value
#         #调用内部的死亡方法
#         if self.hp <= 0:
#             self.__death()
#
#     #私有的死亡方法
#     def __death(self):
#         print(self.name,"死亡")
#         print("游戏结束")
#
#
# class Enemy:
#     def __init__(self,name,hp,ack):
#         self.name = name
#         self.hp = hp
#         self.ack = ack
#
#     def attack(self,other):
#         print(self.name,"攻击",other.name)
#         other.damage(self.ack)
#
#     def damage(self,value):
#         print(self.name,"被攻击,受伤掉血")
#         self.hp -= value
#         if self.hp <= 0:
#             self.__death()
#
#     def __death(self):
#         print(self.name, "死亡")
#         print("掉装备加分")
#
# er01 = Player("玩家01",100,15)
# en01 = Enemy("敌人01",20,5)
# er01.attack(en01)
# en01.attack(er01)
# er01.attack(en01)