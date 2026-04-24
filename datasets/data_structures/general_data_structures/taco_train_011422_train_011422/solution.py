for _ in range(int(input())):
	N = int(input())
	A = input().split()
	counter = 0
	sum = 0
	t = 0
	i = 0
	while i < N:
		if A[i] == '0':
			counter = counter + 1
			t = 1
		elif A[i] == '1' and t == 1:
			if sum < counter:
				sum = counter
			else:
				sum = sum + 1
		i = i + 1
	print(sum)
