from sys import stdin
from math import *
from sys import stdout
line = stdin.readline().rstrip().split()
m = int(line[0])
n = int(line[1])
bits = []
for i in range(n):
	print(m)
	stdout.flush()
	line = stdin.readline().rstrip().split()
	res = int(line[0])
	if res == 0:
		exit(0)
	if res == 1:
		bits.append(-1)
	else:
		bits.append(1)
minN = 1
maxN = m
i = 0
while True:
	current = int((minN + maxN) / 2)
	print(current)
	stdout.flush()
	line = stdin.readline().rstrip().split()
	res = int(line[0])
	if res == 0:
		exit(0)
	res *= bits[i]
	i = (i + 1) % n
	if res == 1:
		minN = current + 1
	else:
		maxN = current - 1
