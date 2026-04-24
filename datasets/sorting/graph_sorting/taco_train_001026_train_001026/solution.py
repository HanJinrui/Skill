n = int(input())
a = sorted(zip(map(int, input().split()), range(n)))
s = []
for i in range(n):
	if a[i]:
		s.append([])
		while a[i]:
			s[-1].append(i + 1)
			(a[i], i) = (None, a[i][1])
print(len(s))
for l in s:
	print(len(l), *l)
