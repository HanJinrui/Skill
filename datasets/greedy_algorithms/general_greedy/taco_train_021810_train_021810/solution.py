class Solution:

	def LexicographicallyMinimum(self, str):
		a = str
		res = a
		l1 = list(a)
		l2 = set(a)
		l2 = list(l2)
		l2.sort()
		x = 0
		for i in range(len(a)):
			if x == len(l2):
				break
			if ord(l1[i]) > ord(l2[x]):
				res = a.replace(l1[i], '0').replace(l2[x], l1[i]).replace('0', l2[x])
				break
			if ord(l1[i]) == ord(l2[x]):
				x += 1
		return res
