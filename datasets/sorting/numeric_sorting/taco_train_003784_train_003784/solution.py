I = lambda : map(int, input().split())
(n, k) = I()
r = 0
a = []
for i in I():
	r += i // 10
	a += [i % 10]
for i in sorted(a, reverse=1):
	if i + k > 9:
		k = k - 10 + i
		r += 1
print(min(n * 10, r + k // 10))
