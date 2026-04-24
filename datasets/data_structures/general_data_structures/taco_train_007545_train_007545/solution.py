def save_gotham(arr, n):
	st = [arr[0]]
	ans = 0
	for i in arr[1:]:
		while st and i > st[-1]:
			st.pop()
			ans += i
		st.append(i)
	return ans
