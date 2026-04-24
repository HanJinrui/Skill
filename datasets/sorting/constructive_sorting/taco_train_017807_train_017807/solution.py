import sys
input = sys.stdin.readline
for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	if a == sorted(a):
		print(0)
		continue
	m = 0
	ans = []
	p = a[0] & 1
	l = -1
	li = -1
	for i in range(n - 1, -1, -1):
		if a[i] & 1 == p:
			if l == -1:
				l = a[i]
				li = i
			elif a[i] > l:
				a[i] = l
				m += 1
				ans.append([i + 1, li + 1])
			else:
				l = a[i]
				li = i
	t = 0
	for i in range(1, n):
		if a[i] & 1 != p:
			m += 1
			ans.append([t + 1, i + 1])
		else:
			t = i
	print(m)
	for i in ans:
		print(*i)
