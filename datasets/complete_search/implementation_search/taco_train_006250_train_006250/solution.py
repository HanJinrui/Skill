n = int(input())
for k in range(9):
	d = 2 * 2 ** k - 1 << k
	if n % d == 0:
		ans = d
print(ans)
