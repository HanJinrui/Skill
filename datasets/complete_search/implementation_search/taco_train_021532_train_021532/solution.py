(na, ma) = map(int, input().split())
ta = [int(input(), 2) for i in range(na)]
(nb, mb) = map(int, input().split())
tb = [input() for i in range(nb)]
(x, y) = ('0' * (ma - 1), '0' * (2 * (ma - 1) + mb))
t = [y] * (na - 1) + [x + tb[i] + x for i in range(nb)] + [y] * (na - 1)
ans = -1
for i in range(na + nb - 1):
	for j in range(ma + mb - 1):
		s = sum((bin(int(t[i + k][j:j + ma], 2) & ta[k]).count('1') for k in range(na)))
		if s > ans:
			ans = s
			(x, y) = (j, i)
print(y - na + 1, x - ma + 1)
