for p in range(int(input())):
	n = int(input())
	r = 0
	a = list(map(int, input().split()))
	for i in range(len(a)):
		for j in range(i):
			if a[j] >= a[i]:
				r += 1
	print(r)
