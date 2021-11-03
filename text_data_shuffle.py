from __future__ import print_function

import sys
with open('input.txt') as file:
	lines = file.readlines()
	lines = [line.rstrip() for line in lines]

f=open('input_128.txt','w')
count=0
for line in lines:
	sys.stdout = f
	print(line, end=' ')
	count=count+1
	if(count==4):
		print(" ")
		count=0
