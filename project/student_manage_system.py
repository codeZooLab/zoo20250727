"""
    学生管理系统
"""

#定义数据模型类
class StudentModel:
    """
    学生模型
    """
    def __init__(self,name = "",age = 0 ,score = 0,id = 0):
        """
        创建学生对象
        """
        self.id = id
        self.name =name
        self.age = age
        self.score = score

#定义系统逻辑控制类
class StudentManageController:
    """
    学生管理控制器，负责业务逻辑处理
    """
    #类变量，表示初始编号
    __init_id =100
    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        """
        学生列表
        :return: 存储学生对象的列表
        """
        return  self.__stu_list

    def __generate_id(self):
        """
        编号生成器
        :return:返回最新编号
        """
        StudentManageController.__init_id += 1
        return  StudentManageController.__init_id

    def add_student(self,stu_info):
        """
        添加一个新学生
        :param stu_info:学生信息
        """
        stu_info.id = self.__generate_id()
        self.__stu_list.append(stu_info)

    def remove_student(self,stu_id):
        """
        根据编号移除信息
        :param stu_id: 编号
        :return: 是否删除成功
        """
        for item in self.__stu_list:
            if item.id == stu_id:
                self.__stu_list.remove(item)
                return True
        return False
        # for i in range(len(self.__stu_list)-1,-1,-1):
        #     if self.__stu_list[i].id == stu_id:
        #         del self.__stu_list[i]

    def update_student(self,stu_info):
        """
        根据编号更改信息
        :param stu_info: 更改后的学生信息
        :return:   是否修改成功
        """
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    def order_by_score(self):
        """
        根据成绩升序
        """
        for r in range(len(self.__stu_list) - 1):
            for c in range(r + 1, len(self.__stu_list)):
                if self.__stu_list[r].score >  self.__stu_list[c].score:
                    self.__stu_list[r],self.__stu_list[c] = self.__stu_list[c],self.__stu_list[r]

#测试数据
# manage = StudentManageController()
# stu01 = StudentModel("张三",18,90)
# manage.add_student(stu01)
# manage.add_student(StudentModel("李四",17,50))
# manage.add_student(StudentModel("王五",20,70))
#新增
# for i in manage.stu_list:
#     print(i.id,i.name,i.age,i.score)
#删除
# print(manage.remove_student(101))
# for i in manage.stu_list:
#     print(i.id,i.name)
#修改
# for i in manage.stu_list:
#     print(i.id,i.name,i.age,i.score)
# manage.update_student(StudentModel("张老三",19,82,101))
# for i in manage.stu_list:
#     print(i.id,i.name,i.age,i.score)
#升序
# manage.order_by_score()
# for i in manage.stu_list:
#     print(i.id,i.name,i.age,i.score)


#界面视图类
class StudentMangeView:
    """
    学生管理器视图
    """
    def __init__(self):
        self.__manage = StudentManageController()

    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩升序显示学生")

    def __select_menu(self):
        item = int(input("请输入:"))
        if item == 1:
            self.__input_student()
        elif item == 2:
            self.__output_student(self.__manage.stu_list)
        elif item == 3:
            self.__delete_student()
        elif item == 4:
            self.__modify_student()
        elif item == 5:
            self.__order_by_output_student()

    def main(self):
        """
        界面试图入口
        调用菜单展示和选择菜单方法
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        name = input("请输入名称")
        age = int(input("请输入年龄"))
        score = float(input("请输入成绩"))
        stu = StudentModel(name,age,score)
        self.__manage.add_student(stu)

    def __output_student(self,list_output):
        for item in list_output:
            print(item.id,item.name,item.age,item.score)

    def __delete_student(self):
        id = int(input("请输入删除的id"))
        if self.__manage.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        id = int(input("请输入需要修改学生编号"))
        name = input("请输入名称")
        age = int(input("请输入年龄"))
        score = float(input("请输入成绩"))
        stu = StudentModel(name,age,score,id)
        if self.__manage.update_student(stu):
            print("更新成功")
        else:
            print("更新失败")

    def __order_by_output_student(self):
        self.__manage.order_by_score()
        self.__output_student(self.__manage.stu_list)

view = StudentMangeView()
view.main()