

def fun02():
    print("b--fun02")

from learning_foundation.package.common.module_b import PrintStr
if __name__ == "__main__":
    p01 = PrintStr("张三")
    p01.get_name()