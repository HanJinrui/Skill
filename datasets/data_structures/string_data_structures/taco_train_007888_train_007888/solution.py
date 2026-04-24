class Solution:

	def SortedString(self, s: str) -> str:
		v = []
		c = []
		res = 'aeiou'
		for i in s:
			if i in res:
				v.append(i)
			else:
				c.append(i)
		v.sort()
		c.sort()
		ans = ''
		if s[0] in v:
			for i in range(len(s)):
				if i < len(v):
					ans += v[i]
				if i < len(c):
					ans += c[i]
		else:
			for i in range(len(s)):
				if i < len(c):
					ans += c[i]
				if i < len(v):
					ans += v[i]
		return ans
