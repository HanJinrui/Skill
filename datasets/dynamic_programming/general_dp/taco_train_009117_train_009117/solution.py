import sys
import numpy as np
MAX = 1000005
a = []
x = []
l = np.zeros(MAX)
r = np.zeros(MAX)
dp = np.zeros(MAX)
last = []
n = int(sys.stdin.readline())
h = sys.stdin.readline().split()
for i in range(1, n + 1):
	p = int(h[i - 1])
	if l[p] == 0:
		l[p] = i
	r[p] = i
for i in range(1, 500001):
	if l[i] and r[i]:
		a.append((l[i], r[i], i))
a.sort()
a.append((n + 7, n + 7, i))
xx = a[0][0]
yy = a[0][1]
ii = a[0][2]
x.append(0)
for i in range(1, len(a)):
	if a[i][0] < yy:
		ii ^= a[i][2]
		if a[i][1] > yy:
			yy = a[i][1]
	else:
		x.append(ii)
		xx = a[i][0]
		yy = a[i][1]
		ii = a[i][2]
n = len(x)
cxor = x[0]
for i in range(MAX):
	last.append(-1)
last[0] = 0
for i in range(1, n):
	cxor ^= x[i]
	if last[cxor] != -1:
		dp[i] = max(dp[i - 1], 1 + dp[last[cxor]])
	else:
		dp[i] = dp[i - 1]
	last[cxor] = i
print(int(dp[n - 1]))
