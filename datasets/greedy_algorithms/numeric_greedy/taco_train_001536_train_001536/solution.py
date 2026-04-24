from sys import stdin, stdout

def calc(c, y):
	if 1 < c <= y:
		return [c]
	B = []
	z = 2
	while z * z <= c:
		if c % z == 0 and 1 < c // z <= y:
			B.append(c // z)
			B.append(z)
			c = 1
			break
		z += 1
	while z >= 2 and c > 1:
		if c % z == 0 and 1 < z <= y:
			while c % z == 0 and c > y:
				B.append(z)
				c //= z
		if 1 < c <= y:
			B.append(c)
			c = 1
			break
		z -= 1
	if c > 1:
		return None
	return sorted(B)

def solve(c, x, n):
	y = x
	A = []
	while c % y == 0:
		c //= y
		A.append(y)
		B = calc(c, y)
		if B is not None:
			X = sorted(B) + A[::-1]
			m = len(X)
			if m <= n:
				res = [1] * (n - m) + X
				return [e + i for (i, e) in enumerate(res)]
		y += 1
	return None

def main():
	t = stdin.readline()
	t = int(t)
	while t > 0:
		(n, c) = map(int, stdin.readline().split())
		x = 1
		ans = None
		while x * x <= c:
			if c % x == 0:
				res = solve(c, x, n)
				if res is not None:
					ans = res
					break
			x += 1
		else:
			while x >= 1:
				if c % x == 0:
					res = solve(c, c // x, n)
					if res is not None:
						ans = res
						break
				x -= 1
		print(' '.join(map(str, ans)))
		t = t - 1
main()
