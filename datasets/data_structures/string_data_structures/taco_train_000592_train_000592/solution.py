def isValid(s):
	nums = s.split('.')
	if len(nums) != 4:
		return 0
	for num in nums:
		if not num.isdigit() or int(num) > 255 or (num[0] == '0' and len(num) > 1):
			return 0
	return 1
