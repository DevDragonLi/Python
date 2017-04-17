#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

print abs(-1010)
print max(1,3,33983)

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

absResult = abs  
absResult(2002)

# 定义函数 
'''
定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
然后，在缩进块中编写函数体，函数的返回值用return语句返回
'''
def functionName(int,int):
	print 