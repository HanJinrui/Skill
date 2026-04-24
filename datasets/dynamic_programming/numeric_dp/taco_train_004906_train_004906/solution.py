primes = []
for i in range(2, 10 ** 5):
	x = 0
	for j in range(2, int(i ** 0.5) + 1):
		if i % j == 0:
			x = 1
			break
	if x == 0:
		primes.append(i)
set_p = set(primes)
n = int(input())
a = list(map(int, input().split()))
a = a[::-1]
ans = 0
store = {}
c = 0
for i in a:
	c = 0
	b = set()
	if i == 1:
		ans = max(ans, 1)
	x = i
	for i in primes:
		if x == 1:
			break
		if x in set_p:
			b.add(x)
			break
		if x % i == 0:
			b.add(i)
			while x % i == 0:
				x = x // i
	for i in b:
		if i in store:
			c = max(c, store[i] + 1)
		else:
			c = max(c, 1)
	for i in b:
		store[i] = c
	if c > ans:
		ans = c
print(ans)
