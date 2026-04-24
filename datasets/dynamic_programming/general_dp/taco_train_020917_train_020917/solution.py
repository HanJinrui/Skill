import sys
from array import array

def input():
	return sys.stdin.buffer.readline().decode('utf-8')
(n, m) = map(int, input().split())
flag = [tuple(map(lambda c: ord(c) - 97, input().rstrip())) for _ in range(n)]
dp = [[[m] * 26 for _ in range(26)] for _ in range(n)]
for i in range(n):
	for j in range(m):
		if j & 1 == 0:
			for k in range(26):
				dp[i][flag[i][j]][k] -= 1
		else:
			for k in range(26):
				dp[i][k][flag[i][j]] -= 1
	if i > 0:
		for j in range(26):
			left = [10 ** 5 * 3] * 26
			right = [10 ** 5 * 3] * 27
			for x in range(26):
				if j == x:
					continue
				for y in range(26):
					if x == y:
						continue
					if y > 0 and left[y - 1] > dp[i - 1][x][y]:
						left[y - 1] = dp[i - 1][x][y]
					if right[y + 1] > dp[i - 1][x][y]:
						right[y + 1] = dp[i - 1][x][y]
			for k in range(24, -1, -1):
				if left[k] > left[k + 1]:
					left[k] = left[k + 1]
			for k in range(26):
				dp[i][j][k] += left[k] if left[k] < right[k] else right[k]
				if right[k] < right[k + 1]:
					right[k + 1] = right[k]
ans = 10 ** 9
(p_i, p_j) = (-1, -1)
for i in range(26):
	for j in range(26):
		if i == j:
			continue
		if ans > dp[-1][i][j]:
			ans = dp[-1][i][j]
			(p_i, p_j) = (i, j)
new_flag = []
for i in range(n - 1, -1, -1):
	row = (chr(97 + p_i) + chr(97 + p_j)) * (m >> 1) + (chr(97 + p_i) if m & 1 else '')
	new_flag.append(row)
	if i:
		min_v = 10 ** 9
		(n_i, n_j) = (-1, -1)
		for j in range(26):
			if p_i == j:
				continue
			for k in range(26):
				if p_j != k and j != k and (min_v > dp[i - 1][j][k]):
					min_v = dp[i - 1][j][k]
					(n_i, n_j) = (j, k)
		(p_i, p_j) = (n_i, n_j)
print(ans)
for row in reversed(new_flag):
	print(row)
