import re

# re.findall()    以列表的形式，尽可能返回结果
str1 = "hello 113 \n   \t world 123"
res = re.findall('hello', str1)
print(res)
# .除了\n的所有内容都能提取到
res = re.findall('.', str1)
print(res)
# \d 匹配所有数字
res = re.findall('\d', str1)
print(res)
# \D  除了数字所有的
res = re.findall('\D', str1)
print(res)
# \w 匹配字母数字下划线
res = re.findall('\w', str1)
print(res)
# \W 匹配非字母数字下划线
res = re.findall('\W', str1)
print(res)
# []  返回符合括号中的内容
res = re.findall('[1-9a-z]', str1)
print(res)
# |  匹配任意一边的内容
res = re.findall('hello|world', str1)
print(res)
# （）组匹配
res = re.findall('(\w)l', str1)
print(res)
str2 = '123 444 555'
res = re.findall('(\d)4', str2)
# res=re.findall('(?P<id>\d)4',str2)
# res=re.findall('(?P<id>\d)4(?P=id)',str2)
print(res)

# 长度匹配
# * 匹配0 个或者 多个
res = re.findall('\d*', str1)
print(res)
# +匹配一个或者多个
res = re.findall('\d+', str1)
print(res)
# ？匹配0个或者1个
res = re.findall('\d?', str1)
print(res)
# {} 匹配多次，匹配括号内指定的次数
res = re.findall('\d{3}', str1)
print(res)
# 特殊匹配
# ^ 匹配以什么开头
res = re.findall("^hello", str1)
print(res)
# $ 匹配以什么结束
res = re.findall("123$", str1)
print(res)
