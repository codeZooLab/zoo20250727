"""
    装饰器
"""
import time
# 需求：对以下两个功能增加权限验证.
"""
# 需要增加的功能
def verify_permissions():
    print("权限验证")

# 已有功能
def enter_background():
    verify_permissions()
    print("进入后台")

def delete_order():
    verify_permissions()
    print("删除订单")

enter_background()
delete_order()

# 缺点：增加新功能，需要修改已有功能．  [违反开闭原则]
"""

"""
# 需要增加的功能
def verify_permissions(func):
    def wrapper():
        print("权限验证")
        func()
    return wrapper

# 已有功能
def enter_background():
    print("进入后台")

def delete_order():
    print("删除订单")

# enter_background = 新功能 + 旧功能
enter_background = verify_permissions(enter_background)
delete_order = verify_permissions(delete_order)

enter_background()
delete_order()
缺点：每次拦截对已有功能(enter_background)的调用,不科学.
"""

"""
# 需要增加的功能
def verify_permissions(func):
    def wrapper():
        print("权限验证")
        func()
    return wrapper

# 已有功能
# enter_background = verify_permissions(enter_background)
@verify_permissions
def enter_background():
    print("进入后台")

@verify_permissions
def delete_order():
    print("删除订单")

enter_background()
delete_order()
缺点：如果已有功能参数不统一，则无法包装.
"""
# def verify_permissions(func):
#     def wrapper(*args, **kwargs):
#         print("权限验证")
#         func(*args, **kwargs)
#     return wrapper
#
# # 已有功能
# @verify_permissions
# def enter_background(login_id, pwd):
#     print(login_id, pwd, "进入后台")
#
# @verify_permissions
# def delete_order(id):
#     print("删除订单", id)
#
# enter_background("abc", 1234)
# delete_order(101)


# # 练习1
# def auth(func):
#     def wrapper(*args,**kwargs):
#         print("账号验证")
#         func(*args,**kwargs)
#     return wrapper
# @auth
# def deposit(money):
#     print("存%s钱"%money)
#
# @auth
# def withdraw(login_id,pwd):
#     print("取钱",login_id,pwd)
#
# deposit(1000)
# withdraw("abc",123)

def print_execute_time(fun):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = fun(*args,**kwargs)
        execute_time = time.time() - start_time
        print(execute_time)
        return result
    return wrapper

# 练习2
@print_execute_time
def funo1():
    time.sleep(2)
    print("fun01执行完成")
@print_execute_time
def fun02(a):
    time.sleep(1)
    print("fun02执行完成,参数:是",a)

funo1()
fun02(100)

