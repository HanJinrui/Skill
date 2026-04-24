P1 = 1000000007
P2 = 1000000009
t = int(input())
for test in range(t):
	n = int(input()) - 1
	a = pow(n, 2) + n
	b = 4 * n - 2
	print(a % P1 * pow(b, P1 - 2, P1) % P1, a % P2 * pow(b, P2 - 2, P2) % P2)
