from collections import Counter

class Solution:

	def isCircle(self, N, A):
		c0 = Counter((a[0] for a in A))
		c1 = Counter((a[-1] for a in A))
		if c0 != c1:
			return 0
		d = {}
		for a in A:
			d.setdefault(a[0], set()).add(a[-1])
		(r, *_) = d
		q = {r}
		done = set()
		while q:
			r = q.pop()
			done.add(r)
			q.update(d[r] - done)
		return 1 if done == set(d) else 0
