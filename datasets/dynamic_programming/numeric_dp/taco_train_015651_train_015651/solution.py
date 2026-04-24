n = int(input())
a = list(map(int, input().split()))
l = [0] * (10 ** 6 + 1)
for aa in a:
	l[aa] = 1
for i in range(n):
	if l[a[i]]:
		for x in range(a[i] * 2, 10 ** 6 + 1, a[i]):
			if l[x]:
				l[x] = max(l[x], l[a[i]] + 1)
print(max(l))
