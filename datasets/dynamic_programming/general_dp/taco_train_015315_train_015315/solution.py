import math
import os
import random
import re
import sys

def unfairGame(s):
	nimSum = 0
	for i in s:
		nimSum ^= int(i)
	if nimSum == 0:
		return 0
	print(s)
	divider = 2 ** (len(bin(nimSum)) - 3)
	print(divider)
	modlist = [x % divider if x % (2 * divider) < divider else -1 for x in s]
	print(modlist)
	if max(modlist) < 0:
		s[s.index(max(s))] += divider
		return divider + unfairGame(s)
	increaseNumber = max(modlist)
	increase = divider - increaseNumber
	print(increase)
	s[modlist.index(increaseNumber)] += increase
	print(s)
	print()
	return increase + unfairGame(s)
fptr = open(os.environ['OUTPUT_PATH'], 'w')
t = int(input().strip())
for t_itr in range(t):
	s_count = int(input().strip())
	s = list(map(int, input().rstrip().split()))
	result = unfairGame(s)
	fptr.write(str(result) + '\n')
fptr.close()
