from itertools import accumulate
primes = [1 for _ in range(pow(10, 7) + 1)]
(primes[0], primes[1]) = (0, 0)
for num in range(2, 4 * pow(10, 3)):
	if primes[num] == 1:
		for x in range(2 * num, pow(10, 7) + 1, num):
			primes[x] = 0
primes[2] = 0
prime_cnt = list(accumulate(primes))
for _ in range(int(input())):
	n = int(input())
	print(prime_cnt[n] - prime_cnt[n // 2] + 1)
