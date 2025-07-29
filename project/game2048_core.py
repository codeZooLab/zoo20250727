"""
2048游戏核心算法
"""

#零元素移置末尾
def zero_to_end():
    for i in range(len(list_merge)-1,-1,-1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)

#将相邻的相同数字合并
def merge_num():
    zero_to_end()
    for i in range(len(list_merge)-1):
        if list_merge[i] == list_merge[i+1]:
            list_merge[i] += list_merge[i+1]
            del list_merge[i+1]
            list_merge.append(0)


#地图向左移动
def remove_left():
    for list_i in map:
        global list_merge
        list_merge = list_i
        merge_num()

#地图向右移动
def remove_right():
    for list_i in map:
        global list_merge
        #从右向左取出数据 形成新列表
        list_merge = list_i[::-1]
        merge_num()
        #从右向左接收 合并后的数据
        list_i[::-1] = list_merge

#方针转置
def policy_transposition():
    for c in range(1, len(map)):
        for r in range(c, len(map)):
            map[r][c - 1],map[c - 1][r] = map[c - 1][r],map[r][c - 1]

#地图向上移动
def remove_up():
    policy_transposition()
    remove_left()
    policy_transposition()

#地图向下移动
def remove_down():
    policy_transposition()
    remove_right()
    policy_transposition()

map=[
    [2,0,0,2],
    [4,4,2,2],
    [2,4,0,4],
    [0,0,2,2]
]

remove_up()
print(map)

