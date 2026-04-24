class Solution:

	def CamelCase(self, N, D, Pat):
		ans = []
		for w in D:
			ext = ''.join((c for c in w if c.isupper()))
			if ext.startswith(Pat):
				ans.append(w)
		return sorted(ans)
