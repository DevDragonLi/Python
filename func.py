#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000

# 调用函数的时候，如果传入的参数数量或者类型不对，会报TypeError的错误  TypeError: abs() takes exactly one argument (2 given)	print abs(100,100)
# print abs(-1010)print max(1,3,33983)
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

absFuncType = abs  
print (absFuncType (-1019))

'''
1. 定义函数 
def:依次写出函数名、括号、括号中的参数和冒号:
然后，在缩进块中编写函数体，函数的返回值用return语句返回如果没有return语句，函数执行完毕后也会返回结果，只是结果为None
'''
number_Global = None  # 先定义为 None,后 global 修饰

def testFunc(number1,number2):
	global number_Global
	if number2 + number1 > 10:
		print "true"
	else :
		print "False"

testFunc(10,20) # testFunc(a = 10,b = 20) detail write way 

testFunc("1","2")  # 参数类型不检查 参数类型做检查，

#格式:	if not isinstance (parmas,(type,type))只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()

def checkFunc(number):
	if not isinstance (number,(int,float)):
	 raise TypeError('bad operand type')
	 print number

checkFunc(22)


def returnMulityParmas(num,num1):
	print (num + num1)
	return num + 1 ,num1 + 3

receiveNum,receivenum2 =  returnMulityParmas(10,19)
print receiveNum,receivenum2   
# Python的函数返回多值其实就是返回一个tuple

#1.1 pass 空函数  
def nop():
    pass
nop

if True >0 :  # 缺少了pass，代码运行就会有语法错误
	pass   
'''
 1.2 函数的参数 :
 		使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
'''
def funcNumberPower(numbe): # 先写一个计算平方的函数：
	print numbe *numbe

funcNumberPower(666)  # 后期如果计算三次方等?

def funcPower(x,n = 2):  # 设置默认值 n = 2
    result = 1
    while n > 0:
        n = n - 1
        result = result * x
    return result

print (funcPower(2,2))
print (funcPower(2,5))
print (funcPower(2))  # 就是2 *2 计算

'''

1.3 可变参数
可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，
参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：

'''
# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# print calc([1, 2, 3])   


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(1,2)

test_nums = [1, 2, 3] # Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去

calc(*test_nums) # *test_nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。


'''
1.4关键字参数 
			允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
			example: 用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求
'''
def person(name, age, **kw):
    if 'city' in kw:# 有city参数
        pass
    if 'job' in kw:# 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Adam', 45, gender='M', job='Engineer')  # dict 

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

''' 
1.4.1 命名关键字  待完善
		参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
		命名关键字参数必须传入参数名
		命名关键字参数可以有缺省值，从而简化调用	
'''


'''
外部模块安装 	: 
	install numpy 	:   `sudo pip3 install numpy`
	uninstall numpy	:	`sudo pip3 uninstall numpy`
	upgrade			: 	`sudo pip3 install -U numpy`
'''


