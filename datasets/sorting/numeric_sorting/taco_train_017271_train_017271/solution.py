def go(m, k):
	(rem, ans, binom) = (m * k, 0, 1)
	ones = 0
	while ones <= k:
		take = min(1 if ones == 0 else rem // ones, binom)
		if take == 0:
			break
		ans += take
		rem -= ones * take
		binom = binom * (k - ones) // (ones + 1)
		ones += 1
	return ans

def solve():
	(n, m) = map(int, input().split())
	ans = 1
	while go(m, ans) < n:
		ans *= 2
	jmp = ans
	while jmp:
		if go(m, ans - jmp) >= n:
			ans -= jmp
		jmp //= 2
	print(ans)
t = int(input())
for _ in range(t):
	solve()
