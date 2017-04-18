#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 调用函数的时候，如果传入的参数数量或者类型不对，会报TypeError的错误  TypeError: abs() takes exactly one argument (2 given)	print abs(100,100)

print abs(-1010)
print max(1,3,33983)

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

absFunc = abs  
print (absFunc (-1019))

# 1. 定义函数 
'''
def:依次写出函数名、括号、括号中的参数和冒号:
然后，在缩进块中编写函数体，函数的返回值用return语句返回

如果没有return语句，函数执行完毕后也会返回结果，只是结果为None
'''
def testFunc(number1,number2):
	if number2 + number1 > 10:
		print "true"
	else :
		print "False"

testFunc(10,20)

testFunc("1","2")  # 参数类型不检查

# 参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()

'''
格式:	if not isinstance (parmas,(type,type)) : 
'''

def checkFunc(number):
	if not isinstance (number,(int,float)):
	 raise TypeError('bad operand type')
	 print number

checkFunc(22)


def returnMulityParmas(num,num1):
	print (num + num1)
	return num + 1 ,num1 + 3

receiveNum,receivenum2 =  returnMulityParmas(10,19)
print receiveNum,receivenum2   # Python的函数返回多值其实就是返回一个tuple

#1.1 pass 空函数  
def nop():
    pass
nop

if True >0 :  # 缺少了pass，代码运行就会有语法错误
	pass   

# 1.2 函数的参数 :使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
# 先写一个计算平方的函数：
def funcNumberPower(numbe):
	print numbe *numbe
	return numbe *numbe
funcNumberPower(666)  # 后期如果计算三次方等呢

def funcPower(x,n = 2):  # 设置默认值 n = 2
    result = 1
    while n > 0:
        n = n - 1
        result = result * x
    return result

print (funcPower(2,2))
print (funcPower(2,5))
print (funcPower(2))  # 就是2 *2 计算

# 可变参数

'''
*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
'''
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc([1, 2, 3])   




