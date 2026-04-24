n = int(input())
c = [1, 0]
s = 0
a = 0
for x in map(int, input().split()):
	if x < 0:
		s = 1 - s
	a += c[s]
	c[s] += 1
print(n * (n + 1) // 2 - a, a)
