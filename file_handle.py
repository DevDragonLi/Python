# -*- coding: utf-8 -*-# \n 换行 

lengTextString = 'this is text string,\n,DragonLi'
print lengTextString

# write a  string  file 
file_test = open('stringFile.txt','w') # w ->write , r -> read , a -> append

file_test.write(lengTextString) # Desktop will create a file  stringFile.txt

file_test.close()  

# read a path file 
file_test_i = open('stringFile.txt','r')
# content = file_test_i.read()
content = file_test_i.readlines()  # line 是一行 
print content
