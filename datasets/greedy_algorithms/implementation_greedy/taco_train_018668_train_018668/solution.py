t = int(input())
for i in range(t):
	(n, m) = map(int, input().split())
	for j in range(m):
		input()
	print('YNEOS'[m >= n::2])
