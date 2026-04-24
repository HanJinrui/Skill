class Solution:

	def solve(self, N):
		e = sorted(list(set(N)))
		t = []
		for i in e:
			t.append((N.count(i), int(i)))
		u = sorted(t)
		return u[-1][-1]
