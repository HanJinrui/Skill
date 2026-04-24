class Solution:

	def UncommonChars(self, A, B):
		A = set(A)
		B = set(B)
		C = ''.join(sorted(A ^ B))
		if C != '':
			return C
		else:
			return -1
