def getStarAndSuperStar(arr, n):
	maxi = max(arr)
	if arr.count(maxi) > 1:
		maxi = -1
	ans = [maxi]
	s = [arr[n - 1]]
	for i in range(n - 2, -1, -1):
		if s[-1] < arr[i]:
			s.append(arr[i])
	return ans + s[::-1]
