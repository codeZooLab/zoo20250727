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