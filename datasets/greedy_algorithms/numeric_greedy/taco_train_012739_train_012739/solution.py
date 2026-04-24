input()
a = [*map(int, input().split())]
c = 0
while a:
	i = a.index(a.pop(0))
	c += i
	del a[i]
print(c)
