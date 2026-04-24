for x in range(int(input())):
	input()
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	z = [a[i] - b[i] for i in range(len(a))]
	print(sum([i for i in z if i > 0]) if sum(z) == 0 else -1)
