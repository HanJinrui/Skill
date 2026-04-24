class Solution:

	def specialPalindrome(self, s1, s2):
		(n, m) = (len(s1), len(s2))
		org = list(s1)
		slis = org[:]
		res = 100000000.0
		for i in range(n - m + 1):
			cur = 0
			for j in range(m):
				if slis[i + j] != s2[j]:
					slis[i + j] = s2[j]
					cur += 1
			cr = range(i, i + m)
			for x in range(n // 2):
				if slis[x] != slis[n - x - 1]:
					if x in cr and n - x - 1 in cr:
						break
					else:
						cur += 1
			else:
				res = min(res, cur)
			slis = org[:]
		return res if res < 100000000.0 else -1
