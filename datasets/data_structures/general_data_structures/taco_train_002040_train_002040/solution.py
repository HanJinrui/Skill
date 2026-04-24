L = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
for i in range(int(input())):
	(a, b) = input().split()
	(a, b) = (int(a), int(b))
	c = str(a + b)
	ans = 0
	for j in c:
		ans += L[int(j)]
	print(ans)
