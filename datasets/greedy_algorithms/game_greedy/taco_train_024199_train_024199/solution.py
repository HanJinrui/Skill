I = input
for i in range(int(I())):
	n = int(I())
	a = [*map(int, I().split())]
	print(['Joe', 'Mike'][n & 1 or a.index(min(a)) & 1])
