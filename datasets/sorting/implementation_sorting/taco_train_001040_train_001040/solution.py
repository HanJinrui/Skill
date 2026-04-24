L = []
input()
p = 1
for i in input().split():
	L += [p] * int(i)
	p += 1
input()
for i in input().split():
	print(L[int(i) - 1])
