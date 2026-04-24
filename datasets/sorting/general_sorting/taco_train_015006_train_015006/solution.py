input()
x = [int(i) for i in input().split()]
for i in range(100):
	print(x.count(i), end=' ')
