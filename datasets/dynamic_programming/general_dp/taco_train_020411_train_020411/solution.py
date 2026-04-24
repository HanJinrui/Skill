(n, m, d) = [int(x) for x in input().split()]
rates = []
for _ in range(n):
	rates.append([int(x) for x in input().split()])
before_peppercorns = [d] * n
before_dollars = [0] * n
after_peppercorns = [None] * n
after_dollars = [None] * n
for t in range(m):
	for i in range(n):
		after_peppercorns[i] = max(before_dollars[i] * rates[i][2 * t + 1], before_peppercorns[i - 1] if i > 0 else 0, before_peppercorns[i + 1] if i < n - 1 else 0, before_peppercorns[i])
		after_dollars[i] = max(before_peppercorns[i] / rates[i][2 * t], before_dollars[i - 1] if i > 0 else 0, before_dollars[i + 1] if i < n - 1 else 0, before_dollars[i])
	for i in range(n):
		before_dollars[i] = after_dollars[i]
		before_peppercorns[i] = after_peppercorns[i]
amt = max(after_peppercorns)
amt2 = max(after_dollars)
if amt > 10 ** 18 or amt2 > 10 ** 18:
	print('Quintillionnaire')
else:
	print(amt)
