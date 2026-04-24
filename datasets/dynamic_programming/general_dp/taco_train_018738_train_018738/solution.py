import math
MOD = int(1000000000.0 + 7)
ans = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

def S_(n, k):

	def cnk(n, k):
		return int(math.factorial(n) // (math.factorial(k) * math.factorial(n - k)))
	return sum((cnk(n, i) for i in range(k, n + 1, 4))) % MOD

def S(n, k=0):
	if n < 5:
		return sum(ans[n][k::4])
	r = pow(2, n - 2, MOD) - pow(2, n // 2, MOD)
	if n & 1:
		r = (r + pow(2, (n - 3) // 2, MOD) * sum(ans[3][(k - (n - 3) // 2) % 4::4])) % MOD
	else:
		r = (r + pow(2, (n - 3) // 2, MOD) * sum(ans[4][(k - (n - 3) // 2) % 4::4])) % MOD
	return int(r)
(n, k) = map(int, input().split())
a = list(map(int, input().split()))
det = [S(i) for i in a]
mem = [[float('+inf')] * (i + 1) for i in range(n + 1)]
mem[0][0] = 1
for i in range(1, n + 1):
	mem[i][1] = sum(det[:i]) % MOD
	mem[i][i] = mem[i - 1][i - 1] * det[i - 1] % MOD
for i in range(3, n + 1):
	for j in range(2, min(i, k + 1)):
		mem[i][j] = (mem[i - 1][j] + mem[i - 1][j - 1] * det[i - 1]) % MOD
print(mem[n][k])
