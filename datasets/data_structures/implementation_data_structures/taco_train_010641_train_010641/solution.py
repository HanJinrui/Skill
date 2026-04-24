input()
a = {}
for i in list(map(int, input().split())):
	while i in a:
		del a[i]
		i *= 2
	a[i] = 1
print(len(a))
print(*a)
