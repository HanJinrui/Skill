from math import factorial
t = int(input())
for t_itr in range(t):
	arr_count = int(input())
	arr = list(map(int, input().rstrip().split()))
	length = len(arr)
	repetitions = length - len(set(arr))
	perm = 0
	for i in range(repetitions + 1):
		perm += (-1) ** i * (factorial(repetitions) // (factorial(i) * factorial(repetitions - i))) * factorial(length - i) // 2 ** (repetitions - i)
	print(perm % (10 ** 9 + 7))
