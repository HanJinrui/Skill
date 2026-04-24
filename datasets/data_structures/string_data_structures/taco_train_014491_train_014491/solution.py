class Solution:

	def findString(self, s):
		cnt = [0] * 26
		for c in s:
			cnt[ord(c) - ord('A')] += 1
		a = ['#'] * 26
		for i in range(26):
			if cnt[i] > 0:
				a[i] = chr(ord('A') + i)
		ans = ''
		diff = 2000
		for i in range(25, -1, -1):
			if a[i] == '#':
				continue
			for j in range(1, 26):
				c = ''
				for k in range(i, -1, -j):
					if a[k] == '#':
						break
					c += a[k]
				if len(c) > len(ans) or (len(c) == len(ans) and diff > j):
					ans = c
					diff = j
		return ans
