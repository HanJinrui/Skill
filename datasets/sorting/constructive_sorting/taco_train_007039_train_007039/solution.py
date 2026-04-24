t = int(input())
for _ in range(t):
	n = int(input())
	nums = []
	for i in range(2 * n - 1):
		(a, b) = map(int, input().split())
		nums.append([b, a, i + 1])
	nums = sorted(nums)[::-1]
	vals = [nums[0][2]]
	i = 1
	while i + 1 < len(nums):
		c = i
		if nums[i][1] < nums[i + 1][1]:
			c = i + 1
		vals.append(nums[c][2])
		i += 2
	print('YES')
	print(*vals)
