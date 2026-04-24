for _ in range(int(input())):
	M = int(input()) - 1
	t = 0
	for m in input().split():
		t |= int(m)
	print((t << M) % 1000000007)
