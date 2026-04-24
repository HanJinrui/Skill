t = int(input())

def func(a):
	ans = 0
	xor = 0
	for _ in range(64):
		for c in a:
			xor = xor ^ c + ans
		if xor == 0:
			return ans
		s = '{0:b}'.format(xor)
		for (i, c) in enumerate(s[::-1]):
			if int(c) == 1:
				ans += 2 ** i
				break
		xor = 0
	return -1
for zzzz in range(t):
	n = input()
	a = [int(x) for x in input().split()]
	print(func(a))
