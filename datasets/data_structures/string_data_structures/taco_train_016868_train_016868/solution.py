for _ in range(int(input())):
	n = int(input())
	s = input()
	a = s[0]
	ans = 1
	for i in s:
		if i != a:
			a = i
			ans += 1
	print(ans // 2)
