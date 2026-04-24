for __ in range(int(input())):
	n = int(input())
	arr = [int(s) for s in input().split()]
	g = 1
	while g < n and arr[g - 1] == arr[g]:
		g += 1
	s = g + 1
	while s + g < n and arr[g + s - 1] == arr[g + s]:
		s += 1
	a = n // 2
	while a > 0 and arr[a] == arr[a - 1]:
		a -= 1
	b = a - g - s
	if b > g:
		print(g, s, b)
	else:
		print(0, 0, 0)
