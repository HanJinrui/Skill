def minSwaps(nums, n):
	k = nums.count(1)
	if k == 0:
		return -1
	s = sum(nums[:k])
	mx = s
	for i in range(k, n):
		s += nums[i]
		s -= nums[i - k]
		mx = max(mx, s)
	return k - mx
