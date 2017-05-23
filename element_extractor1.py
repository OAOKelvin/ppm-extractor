# -*- coding: utf-8 -*-
import re
fname = input('请输入文件名(包括扩展名): ')
eles  = []
while True:
	ele = input('请输入元素名称')
	if str(ele) != 'done':
		eles.append(ele)
	else:break
print(eles)
fhand = open(fname)
for line in fhand:	
	if line.startswith('SampleName=Sample'):
		line = line.split('-')
		num = line[1]
		print ('sample',num)
	else:
		for element in eles:
			Tar = str(element)			
			if line.startswith(Tar):
				print (line[:18])