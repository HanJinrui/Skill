for i in range(eval(input())):
	size, bucket = eval(input()), list(map(int, input().split()))
	res = 0
	bucket.sort()
	for j in range(size):
		 res += abs(bucket[j] - bucket[size/2])
	print(res)
