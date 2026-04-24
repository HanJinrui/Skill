def seive(N):
	junk = set()
	for i in range(2, N+1):
		if i in junk:
			continue	
		primes[i-1] = True
		junk.update( list(range(2*i, N+1, i)) )

n = 10**6

primes = [False] * n
seive(n)
current = 0
cur = 0
k = []
for i in range(1, n+1):
	if primes[i-1]:
		current += 1
	if primes[current-1]:
		cur += 1
	k.append(cur)

T = eval(input())
for i in range(T):
	a, b = list(map( int, input().strip().split() ))
	a -= 1
	b -= 1
	if a == 0:
		print(k[b])
	else:
		print(k[b] - k[a-1])
