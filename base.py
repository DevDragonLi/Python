# -*- coding: utf-8 -*-

# 当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上

import random

teacher = 'DragonLi'

print teacher

teacher = 'LFL'

major = "long"  

combinString = teacher + major   # 合并字符串

print combinString

number = 100
print number

numberTest = 99

result =  (number >= numberTest)

print result

#  if判断 后面 : 不可少  它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else,内部代码需要缩进
if numberTest == number:
	print "equal"
else:
	print "not equal"


while number ==10:  # while : 
	print "equal"

result = (3 >2) and (3 > 1)


# random.randint () ===  随机数

numberRandom = random.randint(1,10)

print numberRandom


number =  True + False
print number

# 在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量，例如：
test = 123 # a是整数
print(test)
test = 'ABC' # a变为字符串
print(test)

'''  
	多行注释   
eg: test = 'DragonLi'

Python解释器干了两件事情：

在内存中创建了一个'DragonLi'的字符串；

在内存中创建了一个名为test的变量，并把它指向'DragonLi'。

'''

# 在Python中，通常用全部大写的变量名表示常量

number = 10
num = 3

print number / num
print number //num


#  ord :函数获取字符的整数表示  chr :函数把编码转换为对应的字符

stringValue =  'Age: %s. Gender: %s' % (25, True)  # 占位符  %S
print stringValue
'''
常见的占位符有：

%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数
'''

# list:Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素

lists = ['xiaolong','xiaoming']

print lists

print len(lists) # 获取长度  ,索引下边从0开始

print lists[1]  # 输出: xiaoming  防止出错,最后一个元素就是 len(lists) - 1

lists.append('long')
lists.insert(1,'second')
print lists

# 要删除list末尾的元素，用pop()方法：
lists.pop(3)	# 删除'long'  指定元素 则(索引)

print lists   


lists = ['test',123,True]  # 元素也可以不同类型
print lists

s = ['python', 'java', ['asp', 'php'], 'scheme'] # list元素也可以是另一个list

print s[2][1]   # 输出--->php

# 另一种有序列表叫元组：tuple。tuple和list非常类似,但是tuple一旦初始化就不能修改,所以代码更安全。如果可能，能用tuple代替list就尽量用tuple

classmates = ('Michael', 'Bob', 'Tracy')
oneTuple = (1,)	# 只有1个元素的tuple定义时必须加一个逗号,
print oneTuple

# 如果tuple 包含list 那么list元素可以修改  (tuple的不可变是指:每个元素指向永远不变!)
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'  
print  t  #('a', 'b', ['X', 'Y'])

# 循环
fors =['111','1111111','e32']

for number_ in fors :
	print number_

# range(5)生成的序列是从0开始小于5的整数 ,xrange(begain,end)
for numhhhh in xrange(1,10):
	print numhhhh


# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
dictionary = {'DragonLi':101 ,'xiaoming':66}

print dictionary

# 通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print dictionary.get('DragonLi') 

dictionary.pop('xiaoming')  # 删除用pop(key)方法，对应的value也会从dict中删除


# 创建一个set，需要提供一个list作为输入集合：重复元素会被过滤
sets = set(['1','2','1'])
print sets  

sets.add('45')

sets.remove('45')




