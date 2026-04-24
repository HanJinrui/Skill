for _ in range(int(input())):
	N = int(input())
	a = list(map(int, input().split()))
	l = r = -1
	for i in range(N - 1):
		if a[i] == a[i + 1]:
			if l == -1:
				l = i
			r = i
	print(0 if l == r else max(1, r - l - 1))
