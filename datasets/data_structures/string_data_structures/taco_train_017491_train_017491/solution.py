class Solution:

	def lps(self, s):
		j = -1
		p = [j]
		for c in s:
			while j >= 0 and s[j] != c:
				j = p[j]
			j += 1
			p.append(j)
		return len(s[:j])
