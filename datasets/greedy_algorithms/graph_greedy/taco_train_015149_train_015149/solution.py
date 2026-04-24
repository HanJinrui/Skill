import sys
input = sys.stdin.readline
for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	d = [0] * n
	c = 0
	for i in range(n):
		if d[a[i] - 1] == 0:
			c += 1
			t = i
			while d[t] == 0:
				d[t] = c
				t = a[t] - 1
	ans = n - c + 1
	for i in range(n - 1):
		if d[i] == d[i + 1]:
			ans -= 2
			break
	print(ans)
