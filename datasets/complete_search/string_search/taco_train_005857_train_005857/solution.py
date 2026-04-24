a = input().split()
print(*a)
for _ in ' ' * int(input()):
	(b, c) = input().split()
	a[a.index(b)] = c
	print(*a)
