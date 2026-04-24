I = input
for _ in [0] * int(I()):
	n = int(I())
	a = [I() for _ in [0] * n]
	print(n - (all((len(s) % 2 ^ 1 for s in a)) & ''.join(a).count('1')))
