for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	a1 = max(a) - max(b)
	if a1 < 0:
		print('NO')
		continue
	a = [max(0, i - a1) for i in a]
	if a == b:
		print('YES')
	else:
		print('NO')
