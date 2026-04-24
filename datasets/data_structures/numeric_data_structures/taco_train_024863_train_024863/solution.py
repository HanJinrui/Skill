MAX = int(1000000.0) + 1
is_prime = [True] * MAX
(a, b) = map(int, input().strip().split())
factor = [list() for _ in range(b - a + 1)]
for i in range(2, MAX):
	if is_prime[i]:
		for j in range(2 * i, MAX, i):
			is_prime[j] = False
		for j in range((a + i - 1) // i * i, b + 1, i):
			factor[j - a].append(i)
(ans, exp) = (0, list())
for i in range(a, b + 1):
	exp.clear()
	k = i
	for x in factor[i - a]:
		c = 0
		while k % x == 0:
			k //= x
			c += 1
		exp.append(c)
	if k > 1:
		exp.append(1)
	while exp:
		(mul, exp) = (1, sorted(exp))
		for x in exp:
			mul *= x + 1
		ans += mul
		exp[-1] -= 1
		if exp[-1] == 0:
			del exp[-1]
print(ans)
