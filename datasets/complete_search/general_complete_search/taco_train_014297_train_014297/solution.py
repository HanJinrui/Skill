numbers = [0]*704978
nums = [0]*91
for i in range(0,91):
	nums[i] = i**3
for i in range(0,91):
	for j in range(i,91):
		test = nums[i]+nums[j]
		if test < 704978:
			numbers[test]+=1
T = int(input())
for t in range(0,T):
	n = int(input())
	for i in range(n,-1,-1):
		if numbers[i] >= 2:
			print(i)
			break
	if i == 0:
		print((-1))
