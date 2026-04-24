from sys import stdin
input()
cnt = [0] * 2 ** 18
t = str.maketrans('0123456789', '0101010101')
for (ch, s) in map(str.split, stdin):
	if ch == '?':
		print(cnt[int(s, 2)])
	else:
		cnt[int(s.translate(t), 2)] += 1 if ch == '+' else -1
