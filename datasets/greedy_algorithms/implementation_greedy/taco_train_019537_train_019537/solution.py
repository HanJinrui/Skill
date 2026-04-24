n = int(input())
Y = sorted(zip(map(int, input().split()), range(1, 1 + n)))
for i in range(n >> 1):
	print(Y[i][1], Y[-1 - i][1])
