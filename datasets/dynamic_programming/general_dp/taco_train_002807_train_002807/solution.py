mod = 10 ** 6 + 3

def prod(a, b):
	return [[sum([a[i][k] * b[k][j] for k in range(len(b))]) % mod for j in range(len(b[0]))] for i in range(len(a))]
(c, w, h) = map(int, input().split())
a = [[0] * (w + 1) for _ in range(w + 1)]
for i in range(w):
	a[i][i + 1] = 1
for cnt in range(0, w + 1):
	a[-1][-1 - cnt] = h ** cnt
ans = [[0] for _ in range(w + 1)]
ans[-1][0] = 1
ans[-2][0] = 1
while c > 0:
	if c % 2 == 1:
		ans = prod(a, ans)
	c = c // 2
	if c > 0:
		a = prod(a, a)
print(ans[-1][0])
