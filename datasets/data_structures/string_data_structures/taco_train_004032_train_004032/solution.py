def missingNumber(s):
	n = len(s)
	for i in range(1, 7):
		miss = 0
		x = s[:i]
		new = ''
		ans = []
		while miss < 2 and s != new:
			if new + x not in s:
				miss += 1
				ans.append(x)
			else:
				new += x
			x = str(int(x) + 1)
		if new == s and len(ans) == 1:
			return ans[0]
	return -1
