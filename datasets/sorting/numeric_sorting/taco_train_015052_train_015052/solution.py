a = (*map(int, [*open(0)][1].split()),)
n = len(a)
s = sum(a)
if s % n:
	exit(print(0))
M = 10 ** 9 + 7
f = [1] * (n + 1)
b = [0] * 3
d = {}
k = 1
for i in range(2, n + 1):
	f[i] = f[i - 1] * i % M
for x in a:
	b[(n * x > s) - (n * x < s)] += 1
	d[x] = d[x] + 1 if x in d else 1
for x in d:
	k *= f[d[x]]
(A, B, C) = b
print([1, f[B] * f[C] * 2 * pow(f[n - A], M - 2, M)][B > 1 and C > 1] * f[n] * pow(k, M - 2, M) % M)
