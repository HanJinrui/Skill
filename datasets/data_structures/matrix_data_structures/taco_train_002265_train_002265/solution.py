def findPerimeter(arr, n, m):
	count = 0
	for i in range(n):
		for j in range(m):
			if arr[i][j]:
				count += i == 0 or not arr[i - 1][j]
				count += i == n - 1 or not arr[i + 1][j]
				count += j == 0 or not arr[i][j - 1]
				count += j == m - 1 or not arr[i][j + 1]
	return count
