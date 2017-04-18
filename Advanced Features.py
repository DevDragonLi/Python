# -*- coding: utf-8 -*-
from collections import Iterable

listNumber = []
n = 100
while n > 0:
	listNumber.append(n)
	n = n -1

print listNumber	# 100 - 1	

#1.切片（Slice）操作符
print listNumber[0:8]  # 从索引0开始取，直到索引8为止，但不包括索引8  [100, 99, 98, 97, 96, 95, 94, 93]

# 如果第一个索引是0，还可以省略：
print listNumber[:8]
print listNumber[1:7]

print listNumber[-3:] # 倒数切片
# 只写[:]就可以原样复制一个list：
listnumber2 = listNumber[10:20]
print listnumber2

# Tuple 字符串也可以
print 'abcde'[1:2]
print (1,3,3,3)[1:2]

# 2.迭代（Iteration) 给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration
dictK = {'frist':'DragonLi','test':'guess'}
for key in dictK.values():  # 默认情况下，dict迭代的是key
	print key    

# 打印出来key 和value
for key,value in dictK.items():
	print key,value


# 判断一个对象是可迭代对象 : 方法是通过collections模块的Iterable类型判断

print  isinstance([1,2,3],Iterable)  # True

# 需要下标  Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
	print i,value   

print "test"

for x,num in [(1,2),(2,3)]:
	print x,num
#3.列表生成式List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
numbers =[1,2,3,4,5]
list(range(1,5))  # 使用range () 
# 生成[1x1, 2x2, 3x3, ..., 10x10]   把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
[x *x for x in range (1,11)]
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
numbers = [x *x for x in range (1,30) if x % 2 == 0]
print numbers

# 列出当前目录下的所有文件和目录名，可以通过一行代码实现

import os
# os.listdir可以列出文件和目录
print [path for path in os.listdir('.')]

print [keyString + '=' + valueString for  keyString,valueString in dictK.items()]

# 一个list中所有的字符串变成小写
strings =['KKK','djjdkd','DragonLi']
print [s.lower() for s in strings]  # 打印出小写的 新list

# 4.生成器 :这种一边循环一边计算的机制，称为生成器：generator
generator = (x * x for x in range(10))




