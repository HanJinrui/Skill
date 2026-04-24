for __ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	print('YES' if all([b[i] >= a[i] and (b[i] == a[i] or b[i] <= b[(i + 1) % n] + 1) for i in range(n)]) else 'NO')
