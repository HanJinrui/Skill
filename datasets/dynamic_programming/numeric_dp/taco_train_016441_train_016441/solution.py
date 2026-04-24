n = 10 ** 7 + 2
s = [1] * n
s[0] = 0
s[1] = 0
for i in range(2, int(n ** 0.5) + 1):
	if s[i]:
		for j in range(2 * i, n, i):
			s[j] = 0
freq = [0] * n
for i in range(2, n):
	freq[i] = freq[i - 1] + s[i]
for i in range(int(input())):
	(x, y) = map(int, input().split())
	ans = y - x - (freq[y] - freq[x + 1])
	print(ans)
