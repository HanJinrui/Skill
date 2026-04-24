(n, k) = map(int, input().split())
if k == 1:
	print(n)
else:
	print(2 ** len(bin(n)[2:]) - 1)
