s = input()
(a, b) = map(int, input().split())
ans = -1
dp = [0] * (len(s) + 1)
p = 1
for i in range(len(s) - 1, -1, -1):
	dp[i] = (dp[i + 1] + int(s[i]) * p) % b
	p = p * 10 % b
p = 0
for i in range(len(s) - 1):
	p = (p * 10 + int(s[i])) % a
	if p == 0 and s[i + 1] != '0' and (dp[i + 1] == 0):
		print('YES')
		print(s[:i + 1])
		print(s[i + 1:])
		exit()
print('NO')
