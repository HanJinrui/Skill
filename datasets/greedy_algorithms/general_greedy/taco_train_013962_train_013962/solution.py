z = [0] * 26
(a, b) = map(int, input().split())
for i in input():
	z[ord(i) - 65] += 1
z.sort(reverse=1 == 1)
s = 0
for i in z:
	k = min(b, i)
	b -= k
	s += k * k
print(s)
