import sys
T = int(input().strip())
for t in range(T):
	N = int(input().strip())
	ar = list(map(int, input().strip().split(' ')))
	m = min(ar)
	print(min((sum(((x + y - m) // 5 + ((x + y - m) % 5 + 1) // 2 for x in ar)) for y in range(5))))
