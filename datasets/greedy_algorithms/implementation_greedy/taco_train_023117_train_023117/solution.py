for _ in range(int(input())):
	(s, k) = input().split()
	(n, k) = (int(s), int(k))
	mark = [0] * 10
	ans = '9' * len(s)
	for i in range(len(s)):
		d = ord(s[i]) - ord('0')
		(d1, d2) = (d + 1, 0)
		if sum(mark) < k:
			if sum(mark) == k - 1 and d1 < 10 and (mark[d1] == 0):
				mark[d1] = 1
				while mark[d2] == 0:
					d2 += 1
				mark[d1] = 0
		else:
			while d1 < 10 and mark[d1] == 0:
				d1 += 1
			while d2 < 10 and mark[d2] == 0:
				d2 += 1
		if d1 < 10:
			ans = min(ans, s[:i] + chr(ord('0') + d1) + chr(ord('0') + d2) * (len(s) - i - 1))
		mark[d] = 1
		if sum(mark) > k:
			break
	if sum(mark) <= k:
		ans = s
	print(int(ans) - n)
