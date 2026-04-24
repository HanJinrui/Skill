import sys
from array import array
from typing import List, Tuple, TypeVar, Generic, Sequence, Union

def input():
	return sys.stdin.buffer.readline().decode('utf-8')

def build_next_table(s):
	s = '*' + s + '*'
	n = len(s) - 1
	kmp = [0] * (n + 1)
	next_table = [[0] * 26 for _ in range(n + 1)]
	for i in range(2, n + 1):
		cur = kmp[i - 1]
		while cur > 0 and s[cur + 1] != s[i]:
			cur = kmp[cur]
		if s[cur + 1] == s[i]:
			cur += 1
		kmp[i] = cur
	alphabet = [chr(cc) for cc in range(97, 123)]
	for i in range(n):
		for (j, c) in enumerate(alphabet):
			cur = i
			while 0 < cur and s[cur + 1] != c:
				cur = kmp[cur]
			if s[cur + 1] == c:
				cur += 1
			next_table[i][j] = cur
	return next_table

def main():
	code = input().rstrip()
	(s, t) = (input().rstrip(), input().rstrip())
	table_s = build_next_table(s)
	table_t = build_next_table(t)
	(n, m, l) = (len(code), len(s), len(t))
	minf = -10 ** 9
	dp = [[array('i', [minf]) * (l + 1) for _ in range(m + 1)] for _ in range(n + 1)]
	dp[0][0][0] = 0
	alphabet = list(range(26))
	for i in range(n):
		itr = [ord(code[i]) - 97] if code[i] != '*' else alphabet
		for j in range(m + 1):
			for k in range(l + 1):
				for cc in itr:
					(nj, nk) = (table_s[j][cc], table_t[k][cc])
					dp[i + 1][nj][nk] = max(dp[i + 1][nj][nk], dp[i][j][k] + (1 if nj == m else 0) - (1 if nk == l else 0))
	ans = minf
	for j in range(m + 1):
		for k in range(l + 1):
			ans = max(ans, dp[n][j][k])
	print(ans)
main()
