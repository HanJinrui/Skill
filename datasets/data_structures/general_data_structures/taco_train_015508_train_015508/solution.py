def main():
	N = int(input())
	a = [int(x) for x in input().split()]
	p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
	c = [[0 for x in range(25)] for y in range(N)]

	def fct(n):
		fact = [0] * 25
		for i in range(25):
			while n % p[i] == 0:
				fact[i] += 1
				n = n // p[i]
			if n == 1:
				return fact
		return fact
	for i in range(N):
		hc = fct(a[i])
		for j in range(25):
			if i > 0:
				c[i][j] = c[i - 1][j] + hc[j]
			else:
				c[i][j] = hc[j]
	for _ in range(int(input())):
		(L, R, M) = map(int, input().split())
		L = L - 1
		R = R - 1
		if L > 0:
			t = [c[R][i] - c[L - 1][i] for i in range(25)]
		else:
			t = [c[R][i] for i in range(25)]
		ans = 1
		for i in range(25):
			ans *= pow(p[i], t[i], M)
			ans %= M
		print(ans)
main()
