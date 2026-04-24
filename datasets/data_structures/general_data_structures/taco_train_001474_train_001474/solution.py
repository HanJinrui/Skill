class Solution:

	def rearrange(self, arr, n):
		pos = [i for i in arr if i >= 0][::-1]
		neg = [i for i in arr if i < 0][::-1]
		arr.clear()
		for i in range(n):
			if len(pos) > 0:
				arr.append(pos.pop())
			if len(neg) > 0:
				arr.append(neg.pop())
