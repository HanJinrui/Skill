from math import floor
n = int(input())
s = [float(input()) for i in range(n)]
l = [*map(floor, s)]
sums = sum(l)
i = 0
while sums:
	if l[i] != s[i]:
		l[i] += 1
		sums += 1
	i += 1
print(*l, sep='\n')
