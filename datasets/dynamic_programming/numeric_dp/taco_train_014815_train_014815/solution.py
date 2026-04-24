def solve():
	MOD = 10 ** 9 + 7
	n = int(input())
	c = list(map(int, input().split()))
	b = [0] + list(map(int, input().split()))
	q = int(input())
	queries = list(map(int, input().split()))
	maxans = 1
	for c1 in c:
		maxans = maxans * (c1 + 1) % MOD
	ans = {}
	for i in range(1, n):
		b[i] += b[i - 1]
	s = lb = 0
	for i in range(1, n):
		s -= b[i]
		lb = min(lb, s // (i + 1))
	s = ub = c[0]
	for i in range(n):
		s += c[i] - b[i]
		ub = min(ub, s // (i + 1))
	for x in queries:
		if x <= lb:
			print(maxans)
		elif x > ub:
			print(0)
		elif x in ans:
			print(ans[x])
		else:
			dp0 = [1] * 10002
			dp0[0] = 0
			bd = 0
			for i in range(n):
				dp1 = [0] * 10002
				bd += b[i] + x
				for j in range(max(bd, 0), 10001):
					dp1[j + 1] = (dp1[j] + dp0[j + 1] - dp0[max(j - c[i], 0)]) % MOD
				dp0 = dp1[:]
			a = dp0[-1]
			ans[x] = a
			print(a)
import sys
input = lambda : sys.stdin.readline().rstrip()
solve()
