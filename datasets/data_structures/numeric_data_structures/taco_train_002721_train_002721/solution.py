from sys import stdin, stdout

def bit_update(bit_a, i, v):
	while i < len(bit_a):
		bit_a[i] += v
		i += i & -i

def bit_query(bit_a, i):
	r = 0
	while i > 0:
		r += bit_a[i]
		i -= i & -i
	return r

def bit_range_query(bit_a, l, r):
	return bit_query(bit_a, r) - bit_query(bit_a, l - 1)
n = int(stdin.readline())
a_a = list(map(int, stdin.readline().split()))
N = max(a_a) + 1
bit_a = [0 for _ in range(N * 2)]
bit_a2 = [0 for _ in range(N * 2)]
p_a = [0] * n
ans = sum = 0
for i in range(1, n + 1):
	x = a_a[i - 1]
	ans += x * (i - 1)
	ans += sum
	sum += x
	ans -= bit_query(bit_a, x)
	j = x
	while j < N:
		l = j
		r = l + x - 1
		ans -= bit_range_query(bit_a2, l, r) * j
		bit_update(bit_a, l, x)
		j += x
	bit_update(bit_a2, x, 1)
	p_a[i - 1] = ans
stdout.write(' '.join(map(str, p_a)))
