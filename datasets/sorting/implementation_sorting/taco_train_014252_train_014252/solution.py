n = int(input())
l = d = 9 ** 9
c = 0
for _ in [0] * n:
	(a, b) = map(int, input().split())
	d &= a <= l
	l = a
	c += a != b
print([['', 'un'][c < 1] + 'rated', 'maybe'][d > 0 == c])
