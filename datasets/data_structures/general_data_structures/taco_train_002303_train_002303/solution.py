from collections import Counter

class Solution:

	def common_element(self, v1, v2):
		ans = []
		a = Counter(v1)
		v2.sort()
		for i in v2:
			if i in a and a[i] > 0:
				ans.append(i)
				a[i] -= 1
		return ans
