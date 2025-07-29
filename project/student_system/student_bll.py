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