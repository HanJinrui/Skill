(n, m, k, t) = map(int, input().split())
k = [list(map(int, input().split())) for i in range(k)]
for i in range(t):
	x = list(map(int, input().split()))
	print('Waste' if x in k else ['Grapes', 'Carrots', 'Kiwis'][(x[0] * m - m + x[1] - sum(map(lambda i: i < x, k))) % 3])
