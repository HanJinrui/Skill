n = int(input())
m = 2 ** 10 - 1
a = 0
b = m
for _ in range(n):
	(op, l) = input().split()
	v = int(l)
	if op == '|':
		a |= v
		b |= v
	elif op == '&':
		a &= v
		b &= v
	else:
		a ^= v
		b ^= v
print(3)
print('&', a | b)
print('|', a & b)
print('^', a & (b ^ m))
