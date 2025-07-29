"""
测试文件注释
"""

"""
# 注释
print("Hello,World!")


#  汇率转换
str1 = input("请输入金额：")
int1 = int(str1)
result = int1 * 6.9
print("结果是:" + str(result))


# 交换变量
data01 = input("请输入变量1：")
data02 = input("请输入变量2：")
# 通用转换
# tmp = data01
# data01 = data02
# data02 = tmp
# 适用python
data01,data02 = data02,data01
print("第一个变量是:" + data01)
print("第二个变量是:" + data02)

# 求找回额度
price = input("商品单价是:")
count = input("商品数量是")
money = input("收入金额:")
result = float(money) - float(price) * int(count)
print("找回金额:" + str(result))

# 求秒数
minutes = int(input("多少分钟:"))
Hour  = int(input("多少小时:"))
day = int(input("多少天:"))
result = minutes * 60 + Hour * pow(60,2) + day * 24 * pow(60,2)
print("总秒数为:" + str(result))

# 求多少斤多少两
liang = int(input("多少两:"))
result1 = liang // 16
result2 = liang % 16
print("为:" + str(result1) + "斤零" + str(result2) + "两" )

# 求加速度
distance = float(input("距离为:"))
time = float(input("时间为:"))
initial_velocity = float(input("初速度为:"))
acceleration = (distance - initial_velocity * time) * 2 / time ** 2
print("加速度为:" + str(acceleration))


# 四位数相加
#  number = int(input("请输入四位数:"))
#  unit01 = number % 10
#  unit02 = number // 10 % 10
#  unit03 = number // 100 % 10
#  unit04 = number // 1000
#  result = unit01 + unit02 + unit03 +unit04
#  print("四位数相加和为:" + str(result))

number = int(input("请输入四位数:"))
result = number % 10
result += number // 10 % 10
result += number // 100 % 10
result += number // 1000
print("四位数相加和为:" + str(result))


# 平年 闰年
year = int(input("请输入年份:"))
result = (year % 4 == 0 and year % 100 != 0 ) or  year % 400 == 0
print(result)


# 求距离
acceleration = float(input("加速度为:"))
initial_velocity = float(input("初速度为:"))
time = float(input("时间为:"))
distance = initial_velocity * time + acceleration * (time ** 2) /2
print("距离为:" + str(distance))

# 摄氏度
fahrenheit = float(input("华氏度为:"))
degree_celsius = (fahrenheit - 32 ) /1.8
print("摄氏度为" + str(degree_celsius))

# 华氏度
degree_celsius = float(input("摄氏度为:"))
fahrenheit = degree_celsius * 1.8 + 32
print("华氏度为" + str(fahrenheit))

# 开氏度
degree_celsius = float(input("摄氏度为:"))
degree_kelvin = degree_celsius + 273.15
print("开氏度为" + str(degree_kelvin))


# 计算天时分
seconds = int(input("秒数为:"))
day = seconds // 86400 # 60*60*24
remaining_seconds = seconds % 86400
Hour = remaining_seconds // 3600
remaining_seconds = seconds % 3600
minutes = remaining_seconds // 60
print(str(day) + "天" + str(Hour) + "小时" + str(minutes) + "分钟")

# 计算时分秒
total_seconds = int(input("秒数为:"))
Hour = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print(str(Hour) + "小时" + str(minutes) + "分钟" + str(seconds) + "秒")

sex = input("输入性别")
if sex == "男":
    print("你好，先生")
elif sex == "女":
    print("你好，女士")
else :
    print("你好，中性人")

# 计算价格
price = float(input("商品单价是:"))
count = int(input("商品数量是"))
money = float(input("收入金额:"))
result = money - price * count
if result >= 0  :
    print("应找回:" + str(result))
else:
    print("金额不足")

# 季度
quarter = input("请输入季度:")
if quarter == "春" :
    print("1、2、3月")
elif quarter == "夏" :
    print("4、5、6月")
elif quarter == "秋" :
    print("7、8、9月")
elif quarter == "冬":
    print("10、11、12月")
else:
    print("错误输入")

# 计算器
int1 = float(input("输入第一个数字:"))
operator = input("输入运算符号:")
int2 = float(input("输入第二个数字:"))
if operator == "+":
    result = int1 + int2
elif operator == "-":
    result = int1 - int2
elif operator == "*":
    result = int1 * int2
elif operator == "/":
    if int2 != 0 :
        result = int1 / int2
    else:
        result ="被除数不能为0"
else:
    result ="运算符错误"
print("结果为" + str(result))

# 比较数大小
int1 = float(input("输入第一个数字:"))
int2 = float(input("输入第二个数字:"))
int3 = float(input("输入第三个数字:"))
int4 = float(input("输入第四个数字:"))
max_int = int1
if max_int < int2:
    max_int = int2
if max_int < int3:
    max_int = int3
if max_int < int4:
    max_int = int4
print(max_int)


# 分数
score = float(input("输入成绩:"))
if score >100 or score < 0 :
    result = '成绩错误'
elif 90 <= score :
    result = '优秀'
elif 75 <= score :
    result = '良好'
elif 60 <= score :
    result = '及格'
else:
    result ='不及格'
print(result)

# 判断天数
month = int(input("输入月份:"))
if month in (1, 3, 5, 7, 8, 10, 12):
    print('31')
elif month in (4, 6, 9, 11):
    print('30')
elif month == 2:
    print('28')
else:
    print('月份有误')


# 真值表达式、条件表达式
# 计算奇偶数
number = int(input("请输入一个数"))
if number % 2 == 1: # 等于if number % 2
    state = "奇数"
else:
    state = "偶数"
print(state)

# 真值
# if number % 2  #bool值1或0 有值没值 
#     state = "奇数"
# else:
#     state = "偶数"
# print(state)

# 条件
# state = '偶数' if int(input("请输入一个数")) % 2 == 0 else '奇数'


# 计算平闰年
year = int(input("请输入年份:"))
# 真值
result = year % 4 == 0 and year % 100 != 0  or  year % 400 == 0
if result:
    day=28
else:
    day=29

# if year % 4 == 0 and year % 100 != 0  or  year % 400 == 0:
#     day=28
# else:
#     day=29

# 不建议可读性太差
# if not year % 4  and year % 100 or not year % 400: #因为整条判断需要结果为true，但如果某条件判断结果值为o时在bool类型中返回为false，所有可以通过添加not取反 来省略判断==0
#     day = 28
# else:
#     day = 29

# day = 28 if year % 4 == 0 and year % 100 != 0  or  year % 400 == 0 else 29
print(day)


# while 循环
while True:  # 死循环：循环条件永远满足
    usd = int(input("输入"))
    print(usd * 1.2)
    if input("输入q键退出:")=="q":
        break  # 退出循环体

# 循环计数
count = 0
while count < 3 :  # 循环计数
    count += 1
    print(count)


# 获取季度
count = 0
while count < 3:
    count += 1
    month = int(input("请输入月份:"))
    if 12 < month or month < 1:
        print("月份错误")
    elif month >= 10:
        print("冬")
    elif month >= 7:
        print("秋")
    elif month >= 4:
        print("夏")
    else:
        print("春")


age = int(input("请输入年龄:"))
if age < 0:
    print("年龄错误")
elif age < 2:
    print("婴儿")
elif age < 13:
    print("儿童")
elif age < 20:
    print("青少年")
elif age < 65:
    print("成年人")
elif age < 150:
    print("老年人")
else:
    print("那不可能")

weight = float(input("请输入体重(kg):"))
height = float(input("请输入身高(m):"))
bmi = weight / height ** 2
if bmi < 18.5:
    print("体重过低")
elif bmi < 24:
    print("正常范围")
elif bmi < 28:
    print("超重")
elif bmi < 30:
    print("1级肥胖")
elif bmi < 40:
    print("2级肥胖")
else:
    print("3级肥胖")
print(bmi)

# 打印中间值
start = int(input("开始值"))
end = int(input("结束值"))
while start < end -1:
    start += 1
    print(start)


# 纸超过珠峰
chickness = 0.01
count = 0
while chickness <= 8844430 :
    count += 1
    chickness *= 2
    # print(chickness)
print(count)


# 猜随机数
import random  # 随机数工具(开头写一次)
random_number = random.randint(1, 100)  # 产生一个随机数
# num01 = None
# count = 0
# while num01 != random_number:
#     num01 = int(input("请输入数字:"))
#     count += 1
#     if num01 < random_number:
#         print("小了")
#     elif num01 > random_number:
#         print("大了")
#     else:
#         print("猜对了，总共猜了" + str(count) + "次")

count = 0
while count < 3:
    #三次内执行
    num01 = int(input("请输入数字:"))
    count += 1
    if num01 < random_number:
        print("小了")
    elif num01 > random_number:
        print("大了")
    else:
        print("猜对了，总共猜了" + str(count) + "次")
        break #退出循环体，不执行else
else:
    #三次以外
    print("游戏结束")


count = 0
while count < 3:
    str_score = input("输入成绩:")
    if str_score == '':
        break
    score = int(str_score)
    if score >100 or score < 0 :
        result = '成绩错误'
        count +=1
    elif 90 <= score :
        result = '优秀'
    elif 75 <= score :
        result = '良好'
    elif 60 <= score :
        result = '及格'
    else:
        result ='不及格'
else:
    print("成绩错误")


# 折纸十次
chickness = 0.01
for chickness in range(10):
    chickness *= 2
print(chickness)


# 累加1-100
sum = 0
for item in range(1,101):
    sum += item
print(sum)

# 累加1-100偶数和
# sum = 0
# for item in range(1,101):
#     if item % 2 == 0:
#         sum += item
# print(sum)

sum = 0
for item in range(2,101,2):
        sum += item
print(sum)

# 累加10-36间的和
sum = 0
for item in range(10,37):
        sum += item
print(sum)


# 三次随机相加 答对加10分
import random  # 随机数工具(开头写一次)
score = 0
for item in range(3):
    random_number1 = int(random.randint(1, 10))  # 产生一个随机数
    random_number2 = int(random.randint(1, 10))  # 产生一个随机数
    sum = int(input("请输入"+str(random_number1)+"+"+str(random_number2)+"="))
    if sum  == random_number1 +random_number2:
        score += 10
print("总分:" + str(score))


# 素数 不考虑2以下
number = int(input("请输入一个数字:"))
for item in range(2,number):
    if number % item == 0:
        print("它不是素数")
        break
else:
    print("它是素数")


# 累加10-50 个位不是2.5.9的数
sum = 0
for item in range(10,51):
    unit = item % 10
    if unit in (2,5,9):
        continue
    sum += item
print(sum)


# str编码
# 字 ————> 数
num01 = ord("a")
print(num01)

# 数 ----》
num01 = chr(97)
print(num01)


str = input("请输入字符串")
for item in str:
    print(ord(item))

while True:
    code = int(input("请输入编码值"))
    if code == '':
        break
    else:
        print(chr(code))

# 字符串格式化 %s %d %f
a = "1"
b = "2"
str01 = "输入" + a + "+" + b + "="  # 字符串拼接(乱)
str02 = "输入%s+%s=" %(a,b)
str03 = "输入%s+%.2f=" %(2,10.55555)
print(str01)
print(str02)
print(str03)


# 索引 不可越界
message = 'wdsafsa'
print(message[3])
print(message[-1])

# 切片 可以越界
message = 'wdsafsa'
print (message[0:3])
print (message[:3]) #开始
print (message[-2:]) #直到末尾
print (message[:]) #全部
print(message[-2:-5:-1]) #倒取
print(message[::-1]) #倒取全部


str = input("输入字符串:")
print(str[0])  #第一个
print(str[-1]) #最后一个
print(str[-3]) #倒数第三个
print(str[:2]) #前两个
print(str[::-1]) #倒序打印
if len(str) % 2 == 1: #如果是奇数，取中间字符
    print(str[len(str) // 2])


name = '悟空'
age = 800
score = 99.5
print("我叫%s,年龄是%d,成绩是%.1f"%(name,age,score))


# 输出边长矩形
num = int(input("输入边长"))
print('''*''' * num)
for item in range(num - 2) :
    print('''*''' + ''' ''' * (num -2) + '''*''' )
print('''*''' * num)


# 判断是否回文 正反向相同
str = input("输入字符串")
if str == str[::-1]:
    print("是")
else:
    print("否")


# 小球100米下落 回弹50米 算回弹多少次 走了多少米
height = 100
distance = height
count = 0
while height / 2 > 0.01:
    count += 1
    distance += height
    height /= 2
print("总共弹起%d次"%count)
print("总共走了%.2f米"%distance)



# 获取名称，等于空字符退出 打印名称一行一个
list02 = []
while True:
    list01 = input("输入人物名称:")
    if list01 == "":
        for item in list02:
            print(item)
        break
    else:
        list02.append(list01)
        


score02 = []
while True:
    score01 = input("输入成绩:")
    if score01 == "":
        for item in score02:
            print(item)
        print("最高分为%.2f,最低分为%.2f,平均分为%.2f"%(max(score02),min(score02),(sum(score02) / len(score02))))
        break
    else:
        score02.append(float(score01))



# 名称存在提示 为空倒序打印
name_list = []
while True:
    name = input("输入姓名:")
    if name in name_list:
        print("名称已存在")
    elif name == "":
        for item in range(len(name_list) - 1, -1, -1):
            print(name_list[item])
        break
    else:
        name_list.append(name)



list01 = [10,20,5,6,88,99]
list02 =[]
for item in list01:
    if item >= 10:
        list02.append(item)
print(list02)


list01 = 0
for item in range(5):
    num = int(input("输入第%d个数字"%(item+1)))
    if num > list01:
        list01 = num
print(list01)



list01 = [10,55,98,23,65]
max_list = list01[0]
for item in list01:
    if item > max_list:
        max_list = item
print(max_list)


#  删除时元素会往前覆盖，注意从后删
list01 = [9, 25, 12, 8]
for i in range(len(list01)-1,-1,-1):
    if list01[i] > 10:
        list01.remove(list01[i])
print(list01)


# 字符串拼接
list01=[]
while True:
    str = input("输入:")
    if str == "":
        break
    else:
        list01.append(str)
print("+".join(list01))


# 字符串拆分
str01 = "how are you"
str02 = str01.split(" ")
print(" ".join(str02[::-1]))


# list01 = [10,55,5,98,23,65]
min_value = list01[0]
for item in list01:
    if item < min_value:
        min_value = item
print(min_value



# 双色球
import random  # 随机数工具(开头写一次)
list01 =[]
while len(list01) < 6 :
    red_num = random.randint(1, 33)  # 随机产生红球
    if red_num not in list01:
        list01.append(red_num)
list01.append(random.randint(1, 16))  # 随机产生篮球
print(list01)


list02 = []
while len(list02) < 6:
    red_num = input("请输入第%d个红球号码"%(len(list02)+1))
    if 1 > int(red_num) or int(red_num) > 33:
        print("号码不在范围中")
    elif red_num in list02:
        print("号码重复")
    else:
        list02.append(red_num)
while len(list02) < 7:
    blue_num = input("请输入蓝球号码")
    if 1 > int(blue_num) or int(blue_num) > 16:
        print("号码不在范围中")
    else:
        list02.append(blue_num)
print(list02)



# 列表推导式
list01 = []
# for i in range(1,11):
#     list01.append(i ** 2)
list01 = [i ** 2 for i in range(1, 11)]  # 添加1-10的平方
list02 = [i for i in list01 if i % 2 != 0]  # 奇数
list03 = [i for i in list01 if i % 2 == 0]  # 偶数
list04 = [i + 1 for i in list01 if i % 2 == 0 and i > 5]  # 偶数大于5加1
print(list01, list02, list03, list04)


# 录入月日，计算是多少天
tuple01 = (31,28,31,30,31,30,31,31,30,31,30,31)
month = int(input("请输入月份:"))
day = int(input("请输入日期:"))
# total_day = day
# for i in range(month-1) :
#     total_day += tuple01[i]
total_day = sum(tuple01[:month - 1]) + day
print(total_day)



# 字典遍历
dict01 = dict([("a","b"),("c","d")])
for key in dict01: #获取key
	print(dict01[key])
for value in dict01.values(): #获取value
	print(value)
for k,v in dict01.items(): #获取键值对key value(元组)
	print(k,v)
	

# 商品价格字典
name_price ={}
while True:
	name =input("输入商品名称:")
	if name =="":
		break
	price = float(input("输入商品价格:"))
	name_price[name] = price
for k,y in name_price.items():
	print("%s的单价是%.2f"%(k,y))

# 字典内嵌列表
dict01 ={}
while True:
	name =input("输入姓名:")
	if name =="":
		break
	age = int(input("输入年龄:"))
	score = float(input("输入成绩:"))
	sex = input("输入性别:")
	# tuple01 = (age,score,sex)
	dict01[name] = [age,score,sex]
for k,y in dict01.items():
	print("%s的年龄是%d,成绩是%.2f,性别是%s"%(k,y[0],y[1],y[2]))


# 字典内嵌字典
dict01 ={}
while True:
	name =input("输入姓名:")
	if name =="":
		break
	age = int(input("输入年龄:"))
	score = float(input("输入成绩:"))
	sex = input("输入性别:")
	dict01[name] = {"age":age,"score":score,"sex":sex}
for k,y in dict01.items():
	print("%s的年龄是%d,成绩是%.2f,性别是%s"%(k,y["age"],y["score"],y["sex"]))


# 列表内嵌字典
list01 =[]
while True:
	name =input("输入姓名:")
	if name =="":
		break
	age = int(input("输入年龄:"))
	score = float(input("输入成绩:"))
	sex = input("输入性别:")
	list01.append({"name":name,"age":age,"score":score,"sex":sex})
for item in range(0,-2,-1):
	dict01 = list01[item]
	if item == 0:
		print("第一个学生%s的年龄是%d,成绩是%.2f,性别是%s"%(dict01["name"],dict01["age"],dict01["score"],dict01["sex"]))
	else:
		print("最后一个学生%s的年龄是%d,成绩是%.2f,性别是%s"%(dict01["name"],dict01["age"],dict01["score"],dict01["sex"]))


# 嵌套循环 字典+列表
dict01={}
while True:
	name = input("请输入姓名:")
	if name == "":
		break
	dict01[name] = []
	while True:
		be_fond_of = input("请输入爱好:")
		if be_fond_of == "":
			break
		dict01[name].append(be_fond_of)
print(dict01)
for k,y in dict01.items():
	result = (",").join(y)
	print("%s的爱好%s"%(k,result))
	

# 1970-2050闰年
year_list = []
for year in range(1970,2051):
	if (year % 4 == 0 and year % 100 != 0 ) or  year % 400 == 0:
		year_list.append(year)
print(year_list)

year_list = [year for year in range(1970,2051) if (year % 4 == 0 and year % 100 != 0 ) or  year % 400 == 0]


# 字典嵌套字典嵌套列表
dict01 = {}
dict01["景区"] = ["故宫","天安门","天坛"]
dict01["美食"] = ["烤鸭","炸酱面","豆汁","卤煮"]
dict02 ={}
dict02["景区"] = ["九寨沟","峨眉山","春熙路"]
dict02["美食"] = ["火锅","串串香","兔头"]
dict03 ={}
dict03["北京"] = dict01
dict03["四川"] = dict02
print(dict03["北京"]["美食"])


# 计算字符出现次数
str01 = "asddqeqehjdjasdageqvvdasdjbdoadjbjqweqw"
dict01 = {}
for i in str01:
    if i not in dict01:
        dict01[i] = 1
    else:
        dict01[i] += 1
print(dict01)


#字段推导式
# dict01 = {}
# for i in range(1,11):
#     if i > 5:
#         dict01[i] = i ** 2
dict01 ={i : i ** 2 for i in range(1,11) if i > 5}



# 字符串长度key value
list01 = ["A","bc","wer","r"]
dict01 = {}
for item in list01:
    dict01[item] = len(item)
print(dict01)

dict02 = {item : len(item) for item in list01}
print(dict02)


# 对号
list01 = ["A","bc","wer","r"]
list02 = [101,102,103,104]
dict01 ={}
for index in range(len(list01)):
    dict01[list01[index]] = list02[index]
print(dict01)
# 通过value找key
dict02 = { value : key for key,value in dict01.items()}  #键值互换 键重复丢失数据
print(dict02)
list03 = [ (value,key) for key,value in dict01.items()]  #转成成列表套元组 保证数据准确
print(list03)


# 集合打印不重复
set01 = set()
while True:
    str01 = input("输入:")
    if str01 == "":
        break
    else:
        set01.add(str01)
print(set01)


seta = {"曹操","刘备","孙权"}
setb = {"曹操","刘备","张飞","关羽"}
print(seta & setb)
print(seta - setb)
print(setb - seta)
print("张飞" in seta)
print(seta ^ setb)
print(len(seta | setb))

#循环打印
for r in range(4):
    for c in range(3):
        print("*#", end ="")
    print()


for r in range(4):
    for c in range(r+1):
        print("*", end ="")
    print()


#排序
list01 = [3,54,63,27,85,2,5,78]
for r in range(len(list01)-1):
    for c in range(r+1,len(list01)):
        if list01[r] > list01[c]:
            list01[r],list01[c] = list01[c],list01[r]
print(list01)


#判断是否存在相同项
list01 = [3,54,63,2,85,10,5,78,99]
result = False
for r in range(len(list01)-1):
    for c in range(r+1,len(list01)):
        if list01[r] == list01[c]:
            print("存在相同项")
            result = True
            break
    if result == True:
        break
if result == False:
    print("不存在相同项")



list01 =[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
print(list01[1][2])  #2行3个
for i in list01[2]:  #3行所有
    print(i)
for item in list01: #每行第一个
    print(item[0])

result =[]
for c in range(len(list01[0])): #矩阵转置 二维列表的列转行
    result.append([])
    for r in range(len(list01)):
        result[c].append(list01[r][c])
print(result)

for c in range(1,len(list01)):  #方针转置
    for r in range(c,len(list01)):
        list01[r][c-1],list01[c-1][r] = list01[c-1][r],list01[r][c-1]
print(list01)


# 列表全排列
list01 = ["a","b","c"]
list02 = ["A","B"]
list03 = []
for i in list01:
    for c in list02:
        list03.append(i+c)
print(list03)
list03 = [i+c for i in list01 for c in list02]  #列表推导式嵌套
print(list03)

"""




