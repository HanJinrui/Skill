MOD = 998244353

def solve():
	(n, k) = map(int, input().split())
	v = list(map(int, input().split()))
	if k > 0 and sum((1 for x in v[-k:] if x > 0)) > 0:
		print('0')
		return
	ans = 1
	for i in range(2, k + 1):
		ans = ans * i % MOD
	for i in range(n - k):
		if v[i] == -1:
			ans = ans * (i + k + 1) % MOD
		if v[i] == 0:
			ans = ans * (k + 1) % MOD
	print(ans)
for _ in range(int(input())):
	solve()
