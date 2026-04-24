n = int(input())
for i in range(n):
	(l, r) = map(int, input().split())
	while l | l + 1 <= r:
		l |= l + 1
	print(l)
