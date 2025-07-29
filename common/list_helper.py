"""
    列表助手模块
"""


class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(list_target, func_condition):
        """
            通用的查找某个条件的所有元素方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件,函数类型
                函数名(参数) --> bool
        :return: 需要查找的元素,生成器类型.
        """
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(list_target, func_condition):
        """
            通用的查找某个条件的单个元素方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件,函数类型
                函数名(参数) --> bool
        :return: 需要查找的元素
        """
        for item in list_target:
            if func_condition(item):
                return item

    @staticmethod
    def get_count(list_target, func_condition):
        """
               通用的计算满足某个条件的元素数量方法
           :param list_target: 需要查找的列表
           :param func_condition: 需要查找的条件,函数类型
                   函数名(参数) --> bool
           :return: 满足条件元素的数量
        """
        count = 0
        for item in list_target:
            if func_condition(item):
                count += 1
        return count

    @staticmethod
    def is_exists(list_target, func_condition):
        """
               通用的判断某个条件是否存在元素满足的方法
           :param list_target: 需要查找的列表
           :param func_condition: 需要判断的条件,函数类型
                   函数名(参数) --> bool
           :return: 是否存在满足的条件 True False
        """
        for item in list_target:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def sum_total(list_target, func_handle):
        """
               通用的求和方法
           :param list_target: 需要求和的列表
           :param func_handle: 需要计算的字段,函数类型
                   函数名(参数) --> int/float
           :return: 总值
        """
        total = 0
        for item in list_target:
            total += func_handle(item)
        return total

    @staticmethod
    def select_handle(list_target, func_handle):
        """
               通用的筛选方法
           :param list_target: 需要筛选的列表
           :param func_handle: 需要筛选的处理逻辑,函数类型
                   函数名(参数1,参数2) --> 任意类型对象
           :return: 生成器
        """
        for item in list_target:
            yield func_handle(item)

    @staticmethod
    def select_max(list_target,func_handle):
        """
               通用的获取最大值的方法
           :param list_target: 需要筛选的列表
           :param func_handle: 需要筛选的处理逻辑,函数类型
                   函数名(参数1)
           :return: 最大元素
        """
        max_value = list_target[0]
        for index in range(1,len(list_target)):
            if func_handle(max_value) < func_handle(list_target[index]) :
                max_value = list_target[index]
        return max_value

    @staticmethod
    def select_min(list_target,func_handle):
        """
               通用的获取最小值的方法
           :param list_target: 需要筛选的列表
           :param func_handle: 需要筛选的处理逻辑,函数类型
                   函数名(参数1)
           :return: 最小元素
        """
        min_value = list_target[0]
        for index in range(1,len(list_target)):
            if func_handle(min_value) > func_handle(list_target[index]):
                min_value = list_target[index]
        return min_value

    @staticmethod
    def orderby_asc(list_target,func_handle):
        """
            通用的升序排列方法
        :param list_target: 目标列表
        :param func_handle: 排序的逻辑
            函数(参数)
        """
        for r in range(len(list_target) -1):
            for c in range(r+1,len(list_target)):
                if func_handle(list_target[r]) > func_handle(list_target[c]):
                    list_target[r],list_target[c] = list_target[c],list_target[r]

    @staticmethod
    def orderby_desc(list_target,func_handle):
        for r in range(len(list_target)-1):
            for c in range(r+1,len(list_target)):
                if func_handle(list_target[r]) < func_handle(list_target[c]):
                    list_target[r],list_target[c] = list_target[c],list_target[r]

    @staticmethod
    def delete_all(list_target, func_condition):
        """
            通用的根据条件删除元素的方法
        :param list_target: 目标列表
        :param func_condition: 删除的逻辑
            函数(参数)
        """
        for i in range(len(list_target)-1,-1,-1):
            if func_condition(list_target[i]):
                del list_target[i]
