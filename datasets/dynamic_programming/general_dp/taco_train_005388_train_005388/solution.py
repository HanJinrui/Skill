from sys import stdin
n = int(input())
s = [stdin.readline()[:-1] for i in range(n)]
cnt = [[0] * 26 for i in range(26)]
for i in range(n):
	t = s[i]
	m = len(t)
	l = ord(t[0]) - 97
	r = ord(t[-1]) - 97
	for i in range(26):
		if cnt[i][l] > 0:
			cnt[i][r] = max(cnt[i][r], cnt[i][l] + m)
	cnt[l][r] = max(cnt[l][r], m)
ans = max([cnt[i][i] for i in range(26)])
print(ans)
