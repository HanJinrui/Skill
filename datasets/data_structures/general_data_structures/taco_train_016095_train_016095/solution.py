class Solution:

	def maxIndexDiff(self, a, n):
		l = [0 for x in range(n)]
		s = []
		s.append(n - 1)
		for i in range(n - 2, -1, -1):
			if a[i] > a[s[-1]]:
				s.append(i)
			else:
				for j in s:
					if a[j] >= a[i]:
						l[i] = j - i
						break
		return max(l)
