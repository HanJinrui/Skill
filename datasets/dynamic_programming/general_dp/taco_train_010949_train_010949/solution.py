class Solution:

	def maxHeight(self, h, w, l, n):
		a = []
		for i in range(n):
			a += [[l[i], w[i], h[i]], [l[i], h[i], w[i]], [w[i], h[i], l[i]], [w[i], l[i], h[i]], [h[i], l[i], w[i]], [h[i], w[i], l[i]]]
		a.sort(reverse=True)
		ans = a[0][2]
		for i in range(1, len(a)):
			x = a[i][2]
			for j in range(i):
				if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
					a[i][2] = max(a[i][2], x + a[j][2])
			ans = max(ans, a[i][2])
		return ans
