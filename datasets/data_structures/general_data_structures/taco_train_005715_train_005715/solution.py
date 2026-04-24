N = int(input())
L = []
for _ in range(N):
	line = input().split()
	if line[0] == 'print':
		print(L)
	else:
		getattr(L, line[0])(*map(int, line[1:]))
