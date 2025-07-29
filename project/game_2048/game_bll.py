"""
    2048游戏逻辑控制器,负责处理游戏核心算法
"""
from project.game_2048.game_model import DirectionModel
from project.game_2048.game_model import Location
import random

class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.__list_empty_location = []

    @property
    def map(self):
        return self.__map

    # 零元素移置末尾
    def __zero_to_end(self):
        """
                    零元素移动到末尾.
        """
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    # 将相邻的相同数字合并
    def __merge_num(self):
        """
                   合并
        """
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    # 地图向左移动
    def __remove_left(self):
        for line in self.__map:
            self.__list_merge = line
            self.__merge_num()

    # 地图向右移动
    def __remove_right(self):
        for line in self.__map:
            # 从右向左取出数据 形成新列表
            self.__list_merge = line[::-1]
            self.__merge_num()
            # 从右向左接收 合并后的数据
            line[::-1] = self.__list_merge

    # 方针转置
    def __policy_transposition(self):
        for c in range(1, len(self.__map)):
            for r in range(c, len(self.__map)):
                self.__map[r][c - 1],self.__map[c - 1][r] = self.__map[c - 1][r],self.__map[r][c - 1]

    # 地图向上移动
    def __remove_up(self):
        self.__policy_transposition()
        self.__remove_left()
        self.__policy_transposition()

    # 地图向下移动
    def __remove_down(self):
        self.__policy_transposition()
        self.__remove_right()
        self.__policy_transposition()

    def move(self,dir):
        """
            移动
        :param dir: 方向 DirectionModel类型
        """
        if dir == DirectionModel.UP:
            self.__remove_up()
        elif dir == DirectionModel.DOWN:
            self.__remove_down()
        elif dir == DirectionModel.LEFT:
            self.__remove_left()
        elif dir == DirectionModel.RIGHT:
            self.__remove_right()

    def generate_new_number(self):
        """
            生成新数字
        """
        self.__get_empty_location()
        if len(self.__list_empty_location) == 0 :
            return -1
        loc = random.choice(self.__list_empty_location) # choice 随机获取一个元素
        # if random.randint(1, 10) == 1:
        #     self.__map[loc.r_index][loc.c_index] = 4
        # else:
        #     self.__map[loc.r_index][loc.c_index] = 2
        self.__map[loc.r_index][loc.c_index] = self.__select_random_number()
        # 因为该位置生成了新数字不是空位置，所以移除该处
        self.__list_empty_location.remove(loc)

    def __select_random_number(self):
        return 4 if random.randint(1, 10) == 1 else 2

    def __get_empty_location(self):
        """
            获取空位置
        """
        # 每次统计空位置，先清空之前的位置，避免影响本次
        self.__list_empty_location.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0:
                    self.__list_empty_location.append(Location(r,c))

    def is_game_over(self):
        """
            游戏是否结束
        :return: False表示没有结束 True表示结束
        """
        # 是否具有空位置
        if len(self.__list_empty_location) > 0:
            return False
        # 横向竖向没有相同的元素
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if c < len(self.__map[r]) -1 and self.__map[r][c] == self.__map[r][c+1]:
                    return False
                if r < len(self.__map) -1 and self.__map[r][c] == self.__map[r+1][c]:
                    return False
        return True

if __name__ == '__main__':
    c01 = GameCoreController()
    c01.move(DirectionModel.UP)
    # print(c01.map)
    c01.generate_new_number()
    print(c01.map)
    print(c01.is_game_over())
