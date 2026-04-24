for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	i = n - 1
	while a[i] == 0 and i > 0:
		i -= 1
	l = 0
	ans = 'No'
	while i >= 0:
		l += a[i]
		if l >= 0:
			break
		i -= 1
	if i == 0 and l == 0:
		ans = 'Yes'
	print(ans)
