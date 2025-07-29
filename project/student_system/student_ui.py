from student_bll import StudentManageController
from student_model import StudentModel


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

    def __input_number(self,message):
        while True:
            try:
                number = int(input(message))
                return number
            except:
                print("值异常,请重新输入")

    def __input_student(self):
        name = input("请输入名称")
        age = self.__input_number("请输入年龄")
        score = self.__input_number("请输入成绩")
        stu = StudentModel(name,age,score)
        self.__manage.add_student(stu)

    def __output_student(self,list_output):
        for item in list_output:
            print(item.id,item.name,item.age,item.score)

    def __delete_student(self):
        id = self.__input_number("请输入删除的id")
        if self.__manage.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        id = self.__input_number("请输入需要修改学生编号")
        name = input("请输入名称")
        age = self.__input_number("请输入年龄")
        score = self.__input_number("请输入成绩")
        stu = StudentModel(name,age,score,id)
        if self.__manage.update_student(stu):
            print("更新成功")
        else:
            print("更新失败")

    def __order_by_output_student(self):
        self.__manage.order_by_score()
        self.__output_student(self.__manage.stu_list)