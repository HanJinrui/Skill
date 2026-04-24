def main():
	(n, k) = map(int, input().split())
	(v, m) = (n - n // k - 1, 0)
	while m < n:
		v += 1
		(m, w) = (0, v)
		while w:
			m += w
			w //= k
	print(v)
main()
