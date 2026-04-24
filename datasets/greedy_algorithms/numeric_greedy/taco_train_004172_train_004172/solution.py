n = int(input())
t = list(map(int, input().split()))
k = t.count(1)
s = ' '.join('1' * k)
p = [0] + [1, 0] * 1000000
for i in range(3, 1415, 2):
	if p[i]:
		p[i * i::2 * i] = [0] * ((2000000 - i * i) // 2 // i + 1)
if k > 1:
	for q in t:
		if q > 1 and p[1 + q]:
			exit(print(k + 1, q, s))
	exit(print(k, s))
for i in range(n):
	for j in range(i + 1, n):
		if p[t[i] + t[j]]:
			exit(print(2, t[i], t[j]))
print(1, t[0])
