# -*- coding: utf-8 -*-

'''
	模块导入:
import time
print (time.localtime())
import time as LFL_time    # adjust name 
print LFL_time.localtime()
只使用某个模块的一个,其他不引用
from time import time,localtime
# print localtime()  // 省略模块名
#  from time import *  all ,省略 time调用
'''

import copy 
# 错误处理  try
try:
	openFile_text = open('DragonLi.txt','r')
except Exception as e:  # [Errno 2] No such file or directory: 'DragonLi.txt'
	print e
else:   # continue if file != nil 
	pass
#  zip 

list_a =[1,2,3]
list_b = [6,7,8]
print zip(list_a,list_b)   # [(1, 6), (2, 7), (3, 8)]

# lambda :handle sample function

def test_add(x,y):
	return x + y 

print test_add(10,20)	

function_add = lambda x,y : x + y 
print function_add(10,20)

# map 
print map(function_add,[1],[2])   # list 
print map(function_add,[1,5],[4,8])


# copy 
list_c = list_a
print ('id -a ',id(list_a),'id - c',id(list_c))  # ('id -a ', 4429911896, 'id - c', 4429911896)
