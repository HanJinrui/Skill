t = int(input())
while t > 0:
	n = int(input())
	b = list(map(int, input().split()))
	ans = 1
	for i in range(n - 1):
		if b[i] > b[i + 1]:
			ans = 0
			break
		ans = ans * (1 << bin(b[i]).count('1')) % (10 ** 9 + 7)
	print(ans % (10 ** 9 + 7))
	t = t - 1
