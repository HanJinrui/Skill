def _solve(n, m, memo):
	if n <= 0:
		return 0
	if n < m:
		return 1
	if n == 1:
		return 2
	if (n, m) in memo:
		return memo[n, m]
	out = 0
	mid = n // 2
	out = (out + _solve(mid, m, memo) * _solve(n - mid, m, memo)) % 1000000007
	for i in range(1, m):
		if mid - i < 0 or n - mid + i - m < 0:
			continue
		n1 = 1 if mid - i == 0 else _solve(mid - i, m, memo)
		n2 = 1 if n - mid + i - m == 0 else _solve(n - mid + i - m, m, memo)
		out = (out + n1 * n2) % 1000000007
	memo[n, m] = out
	return out

def solve(n, m):
	return _solve(n, m, {})

def main():
	from sys import stdin
	(n, m) = list(map(int, stdin.readline().strip().split()))
	out = solve(n, m)
	print('{}'.format(out))
main()
