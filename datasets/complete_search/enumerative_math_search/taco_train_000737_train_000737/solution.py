ul = 10 ** 6
prime = [1] * (ul + 1)
prime[0] = 0
prime[1] = 0
i = 2
while i * i <= ul:
	if prime[i] == 1:
		for j in range(i * i, ul + 1, i):
			prime[j] = 0
	i += 1

def solve(n):
	for pc in range(100, 1, -1):
		if prime[pc] == 0:
			continue
		for ps in range(1000, 1, -1):
			if prime[ps] == 0:
				continue
			el = n - (ps ** 2 + pc ** 3)
			if el > 0 and prime[el] == 1:
				return [el, ps, pc]
	return [0, 0, 0]
while True:
	n = int(input())
	if n == 0:
		break
	print(*solve(n))
