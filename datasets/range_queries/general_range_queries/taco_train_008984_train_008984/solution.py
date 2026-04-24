for i in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	u = 10 ** 9 + 7
	q = int(input())
	if l[0] == 1:
		for i in range(q):
			m = int(input())
			s = 0
			if m % n <= 1:
				s = m // n % u
				if s == 0:
					s = 1
			else:
				s = (m // n + 1) % u
			print(s % 1000000007)
	else:
		dp = [0] * n
		dp[0] = l[0]
		for i in range(1, n):
			dp[i] = dp[i - 1] + l[i]
			if l[i - 1] % 2 != 0 and l[i - 1] > 1:
				dp[i] -= 1
			elif l[i - 1] == 1:
				if l[i - 2] % 2 == 0:
					dp[i] -= 2
		for i in range(q):
			m = int(input())
			s = 0
			if m <= n:
				s = dp[m - 1] % u
			elif m % n == 0:
				s = dp[-1] % u * (m // n % u) % u
				if l[-1] % 2 == 0:
					s -= m // n - 1
			else:
				s = dp[-1] % u * (m // n % u) % u
				if l[-1] % 2 == 0:
					s -= m // n
				s = (s + dp[m % n - 1] % u) % u
			print(s % 1000000007)
