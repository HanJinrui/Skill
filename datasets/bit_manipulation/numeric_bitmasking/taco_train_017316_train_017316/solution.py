t = int(input())
for i in range(t):
	(x, k, answer) = map(int, input().split())
	a = map(int, input().split())
	op = input().strip()
	if k:
		for i in a:
			if op == 'AND':
				answer &= i
			if op == 'OR':
				answer |= i
			if op == 'XOR' and k % 2:
				answer ^= i
	print(answer)
