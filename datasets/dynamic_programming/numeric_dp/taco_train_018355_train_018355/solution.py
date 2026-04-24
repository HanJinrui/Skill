num = input()
num_list = []
for i in range(len(num)):
	num_list.append(int(num[i]))
myMod = 10 ** 9 + 7
length = len(num_list)
f = [0] * (length + 1)
t = [1] * (length + 1)
for i in range(length):
	f[i + 1] = (f[i] * 10 + 1) % myMod
	t[i + 1] = t[i] * 10 % myMod
ans = 0
for i in range(1, 10):
	dp = [0] * (length + 1)
	for j in range(length):
		dp[j + 1] = (dp[j] * i + (10 - i) * (dp[j] * 10 + t[j])) % myMod
	c = 0
	ctr = 0
	for k in num_list:
		z = min(i, k)
		o = k - z
		ans += o * (dp[length - 1 - ctr] * t[c + 1] + f[c + 1] * t[length - 1 - ctr]) % myMod
		ans += z * (dp[length - 1 - ctr] * t[c] + f[c] * t[length - 1 - ctr]) % myMod
		ans %= myMod
		c += k >= i
		ctr += 1
	ans += f[c]
	if ans >= myMod:
		ans -= myMod
print(ans)
