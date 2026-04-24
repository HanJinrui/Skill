from sys import stdin, stdout
import math, sys
from itertools import permutations, combinations
from collections import defaultdict, deque, OrderedDict, Counter
from os import path
import bisect as bi
import heapq
mod = 10 ** 9 + 7

def yes():
	print('YES')

def no():
	print('NO')
if path.exists('input.txt'):
	sys.stdin = open('input.txt', 'r')
	sys.stdout = open('output.txt', 'w')

	def inp():
		return int(input())

	def minp():
		return map(int, input().split())
else:

	def inp():
		return int(stdin.readline())

	def minp():
		return map(int, stdin.readline().split())
n = inp()
a = list(minp())
d = Counter(a)
flag = 0
for keys in d:
	if d[keys] & 1:
		flag = 1
		break
if flag:
	print(-1)
	exit(0)
d = {}
for i in range(2 * n):
	try:
		d[a[i]].append(i + 1)
	except:
		d[a[i]] = [i + 1]
for keys in d:
	print(*d[keys])
