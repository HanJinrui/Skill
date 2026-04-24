import sys
dp1 = [1, 1]
dp2 = [1, 1]
N = 10010
M = 100000000000007
for i in range(2, N):
	dp1.append((3 * (i - 1) * dp1[i - 2] + (2 * i + 1) * dp1[i - 1]) // (i + 2))
	dp2.append(2 * (2 * i - 1) * dp2[i - 1] // (i + 1))
t = int(input())
while t:
	t = t - 1
	(n, k) = input().split()
	if int(k) == 0:
		print('0')
	elif int(k) == 1:
		print((dp1[int(n)] - 1 + M) % M)
	else:
		print((dp2[int(n)] - 1 + M) % M)
