import sys
import bisect
from bisect import bisect_left as lb
from bisect import bisect_right as rb
from queue import PriorityQueue
from queue import Queue
input_ = lambda : sys.stdin.readline().strip('\r\n')
from math import log
from math import gcd
from math import atan2, acos
from random import randint
import random
sa = lambda : input_()
sb = lambda : int(input_())
sc = lambda : input_().split()
sd = lambda : list(map(int, input_().split()))
sflo = lambda : list(map(float, input_().split()))
se = lambda : float(input_())
sf = lambda : list(input_())
flsh = lambda : sys.stdout.flush()
mod = 10 ** 9 + 7
mod1 = 998244353
gp = []
cost = []
dp = []
mx = []
ans1 = []
ans2 = []
special = []
specnode = []
a = 0
kthpar = []

def dfs2(root, par):
	if par != -1:
		dp[root] = dp[par] + 1
	for i in range(1, 20):
		if kthpar[root][i - 1] != -1:
			kthpar[root][i] = kthpar[kthpar[root][i - 1]][i - 1]
	for child in gp[root]:
		if child == par:
			continue
		kthpar[child][0] = root
		dfs(child, root)
ans = 0
a = []
(n, k) = (0, 0)
b = []
vis = []
tot = 0
time = []
time1 = []
adj = []
mx = -1
eps = 1e-07
gp = []
ans = []

def update_it(bit, i, val):
	n = len(bit)
	while i < n:
		bit[i] += val
		i += i & -i

def get_ans(bit, i):
	n = len(bit)
	tot = 0
	while i > 0:
		tot += bit[i]
		i -= i & -i
	return tot

def flip(a, l, r):
	for i in range(l, r):
		a[i] = '0' if a[i] == '1' else '1'
	return

def hnbhai(tc):
	n = sb()
	a = sd()
	a.sort()
	prefix = [0] * n
	for i in range(n):
		prefix[i] = a[i]
		if i > 0:
			prefix[i] += prefix[i - 1]
	dp = [-1] * n
	dp[n - 1] = 0
	for i in range(n - 2, -1, -1):
		for j in range(i + 1, n):
			dp[i] = max(dp[i], dp[j] + (prefix[j - 1] if j - 1 >= 0 else 0) - prefix[i] + a[j] % a[i])
	print(dp[0] + a[0])
	return
for _ in range(sb()):
	hnbhai(_ + 1)
