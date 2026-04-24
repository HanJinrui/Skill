import sys
input = sys.stdin.readline
s = input()
n = len(s)
tree = [0] * (2 * n)
closed = [0] * (2 * n)
opened = [0] * (2 * n)

def build(arr):
	for i in range(n):
		tree[n + i] = 0
		closed[i + n] = int(s[i] == ')')
		opened[i + n] = int(s[i] == '(')
	for i in range(n - 1, 0, -1):
		to_add = min(closed[i << 1 | 1], opened[i << 1])
		tree[i] = tree[i << 1] + tree[i << 1 | 1] + 2 * to_add
		closed[i] = closed[i << 1] + closed[i << 1 | 1] - to_add
		opened[i] = opened[i << 1] + opened[i << 1 | 1] - to_add

def query(l, r):
	left = []
	right = []
	l += n
	r += n
	while l <= r:
		if l & 1:
			left.append((tree[l], opened[l], closed[l]))
			l += 1
		if not r & 1:
			right.append((tree[r], opened[r], closed[r]))
			r -= 1
		l >>= 1
		r >>= 1
	a1 = b1 = c1 = 0
	for (a2, b2, c2) in left + right[::-1]:
		to_match = min(b1, c2)
		a1 += a2 + 2 * to_match
		b1 += b2 - to_match
		c1 += c2 - to_match
	return a1
build(s)
for _ in range(int(input())):
	(a, b) = map(int, input().split())
	print(query(a - 1, b - 1))
