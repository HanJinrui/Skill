def main():
	from math import gcd
	(n, a, l) = (int(input()), 1, [])
	for b in map(int, input().split()):
		if gcd(a, b) > 1:
			l.append(1)
		l.append(b)
		a = b
	print(len(l) - n)
	print(*l)
main()
