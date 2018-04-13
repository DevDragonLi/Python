# -*- coding: utf-8 -*-

class LFL_Class:
	info = 'LFL'

	def __init__(self,name,age = 18):
		self.name = name
		self.ag = age

	def add(self,numberA,numberB):
		result = numberB + numberA
		print result


lfl_instance = LFL_Class('LFL')

lfl_instance.add(10,300)		
print lfl_instance.ag     



		




