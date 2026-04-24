import math
aa = [0 for i in range(1000 * 1000 + 9)]
fact = [0 for i in range(1000 * 1000 + 9)]
indices = []

def SoE():
	for i in range(2, 1000 * 1000 + 1):
		if fact[i] == 0:
			for j in range(i, 1000 * 1000 + 1, i):
				if fact[j] == 0:
					fact[j] = i

def primes(n):
	while n > 1:
		x = 0
		pnum = fact[n]
		while n % pnum == 0:
			x = 1 - x
			n //= pnum
		if x == 1:
			aa[pnum] += 1
			indices.append(pnum)
t = int(input())
SoE()
for i in range(t):
	n = int(input())
	b = list(map(int, input().strip().split()))
	nb2 = n // 2
	for i in b:
		primes(i)
	ans = 0
	for i in indices:
		if aa[i] > nb2:
			ans = ans + n - aa[i]
		else:
			ans += aa[i]
		aa[i] = 0
	print(ans)
	indices = []
