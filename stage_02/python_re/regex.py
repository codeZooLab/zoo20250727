import re

"""
正则表达式 元字符
"""
# print(re.findall('ab','absdaeqefabeqgad'))
# # 元字符| 或关系
# print(re.findall('cn|com','http://www.baidu.com.....cnww'))
# # 元字符. 除换行外任意字符
# print(re.findall('张.丰','张三丰,张四丰a,张\n丰'))
# # 元字符[字符集] 匹配字符集中任意字符
# print(re.findall('[_#0-7a-zA-C]','1_39sdaeqAfZwe#f%'))
# # 元字符[^字符集] 匹配除字符集外任意字符
# print(re.findall('[^_#0-7a-zA-C]','1_39sdaeqAfZwe#f%'))
# # 元字符^ 匹配开头位置
# print(re.findall('^jame','jame,hi'))
# # 元字符$ 匹配结尾位置
# print(re.findall('jame$','hi,jame'))
# # 完全匹配
# print(re.findall('^jame$','jame'))
#
#
# # 重复元字符* 匹配前面的字符出现0次或多次
# print(re.findall('wo*','wooooo~~w!')) # w后面可跟可不跟o
# # 重复元字符+ 匹配前面的字符出现1次或多次
# print(re.findall('wo+','wooooo~~w!')) # w后面最少跟1个o
# # 重复元字符？ 匹配前面的字符出现0次或1次
# print(re.findall('-?[0-9]+','12 -32 127')) # -可有可没有
# # 根据空格拆分取反
# print(re.findall('[^ ]+','Port-9 Error #404# %@STD'))
# # 重复元字符{n} 匹配前面的字符出现n次
# print(re.findall('1[0-9]{10}','张三:18573937730'))
# # 重复元字符{m,n} 匹配前面的字符出现m到n次
# print(re.findall('[1-9][0-9]{5,10}','qq:1643567774'))
#
# # 任意数字\d或非数字\D字符
# print(re.findall('\d{1,5}','port:12334,http:8080'))
# print(re.findall('\D+','port:12334,http:8080'))
#
# # 任意普通字符\w或非普通字符\W
# print(re.findall('\w+','port:12334,http:8080'))
# print(re.findall('\W+','port:12334,http:8080'))
#
# # 任意空字符\s或非空字符\S
# print(re.findall('\w+\s+\w+','Hello   World'))
# print(re.findall('\S+','Hello   World'))
#
# # 开头\A 结尾\Z
# print(re.findall('\AHello','Hello   World'))
# print(re.findall('World\Z','Hello   World'))
#
# # 匹配单词边界位置\b 或非\B
# print(re.findall(r'\bis\b','This is a test'))
# print(re.findall(r'\Bis\b','This is a test'))
#
# # 贪婪与非贪婪模式 加？
# print(re.findall(r'\[.+\]','[aa],[bb],[cc]'))
# print(re.findall(r'\[.+?\]','[aa],[bb],[cc]'))
#
# # 分组->子组->捕获组
# print(re.search(r'(王|李)\w{1,3}','王者荣耀').group())
# print(re.search(r'(https|http|ftp|file)://\S+','http://www.baidu.com').group(1))
# print(re.search(r'(?P<pig>ab)+','abababab').group('pig')) # 捕获组


"""
regex.py  re模块 功能函数演示1
"""
# # 目标字符串
# s = "Alex:1994,Sunny:1999"
# pattern = r"(\w+):(\d+)" # 正则表达式
#
# # re调用函数
# l = re.findall(pattern,s)
# print(l)
#
# # regex表达式对象调用函数
# regex = re.compile(pattern)
# l = regex.findall(s,0,13) # 截取s[0:13]作为匹配目标
# print(l)
#
# # 按照正则匹配的内容,分割目标
# l = re.split(r'[,:]',s)
# print(l)
#
# # 使用字符串替换匹配到的部分
# s = re.subn(r':','-',s,1)
# print(s)


"""
regex1.py re模块 功能函数演示2
生成 match 对象
"""
# s = "今年是2019年,建国70周年"
#
# pattern = r"\d+"
# # 返回迭代对象
# it = re.finditer(pattern,s)
# for i in it:
#     print(i.group()) # 获取match对象对应内容
#
# # 完全匹配
# obj = re.fullmatch(r'.+',s)
# print(obj.group())
#
# # 匹配开始位置
# obj = re.match(r'\w+',s)
# print(obj.group())
#
# # 匹配第一处
# obj = re.search(r'\d+',s)
# print(obj.group())


"""
regex2.py
match对象属性实例
"""
# pattern = r"(ab)cd(?P<pig>ef)"
# regex = re.compile(pattern)
# obj = regex.search("abcdefghi",0,7)  # match对象
#
# # 属性变量
# print(obj.pos)  # 目标字符串开始位置
# print(obj.endpos) # 目标字符串结束位置
# print(obj.re)  # 正则
# print(obj.string) # 目标字符串
# print(obj.lastgroup) # 最后一组组名
# print(obj.lastindex) # 最后一组序号
#
# print("=====================================")
# # 属性方法
# print(obj.span()) # 匹配到的内容在目标字符串中的位置
# print(obj.start())
# print(obj.end())
# print(obj.groups()) # 子组内容对应的元组
# print(obj.groupdict()) # 捕获组字典
# print(obj.group()) # 获取match对象内容
# print(obj.group('pig'))


"""
flags.py 扩展功能标志
"""
s = """Hello
北京"""

# 只能匹配ascii码
# regex = re.compile(r'\w+',flags=re.A)

# 忽略字母大小写
# regex = re.compile(r'[a-z]+',flags=re.I)

# 让 . 可以匹配\n
# regex = re.compile(r'.+',flags = re.S)

# ^ $ 可以匹配每行的开始结束位置
# regex = re.compile(r'Hello$',flags=re.M)

# l = regex.findall(s)
# print(l)

