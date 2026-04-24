class Solution:

	def numoffbt(self, arr, n):
		d = {x: 1 for x in arr}
		a = sorted(d.keys())
		ans = 0
		for i in a:
			for j in range(2 * i, min(i * i + 1, a[-1] + 1), i):
				if j in d and j // i in d:
					temp = d[i] * d[j // i]
					if i * i != j:
						temp = 2 * temp
					d[j] += temp
			ans += d[i]
		return ans % 1000000007
