def main():
	mod = 10 ** 9 + 7
	for _ in range(int(input())):
		n = int(input())
		a = list(map(int, input().split()))
		xx = [0] * (n + 2)
		for i in a:
			xx[i] += 1
		if min(a):
			print(pow(2, n - 1, mod))
			continue
		for i in range(n + 2):
			if not xx[i]:
				m = i
				break
		req = [0] * m
		done = m
		dp = [-1] * n
		i = n - 1
		for j in range(n - 1, -1, -1):
			if a[j] < len(req):
				req[a[j]] += 1
				if req[a[j]] == 1:
					done -= 1
				while i != -1 and (not done):
					dp[i] = j
					if a[i] < len(req):
						req[a[i]] -= 1
						done += req[a[i]] == 0
					i -= 1
		dp1 = [0] * n
		pref = [1] + [0] * n
		for i in range(n):
			if dp[i] != -1:
				dp1[i] = pref[dp[i]]
			pref[i + 1] = (pref[i] + dp1[i]) % mod
		print(dp1[-1])
main()
