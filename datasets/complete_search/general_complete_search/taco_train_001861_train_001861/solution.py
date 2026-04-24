class Solution:

	def combinationalSum(self, A, B):
		k = sorted(list(set(A)))
		l = []

		def f(i, sm, t=[]):
			if sm == 0:
				l.append(list(t))
				return
			for j in range(i, len(k)):
				if sm - k[j] >= 0:
					t.append(k[j])
					f(j, sm - k[j], t)
					t.pop()
				else:
					return
		f(0, B)
		return l
