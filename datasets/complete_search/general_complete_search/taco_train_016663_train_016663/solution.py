for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	sm = 0
	for i in range(n):
		sm += a[i]
		if i >= sm:
			break
	print(sm)
