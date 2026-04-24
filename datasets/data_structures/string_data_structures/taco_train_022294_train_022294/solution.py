class Solution:

	def stringPartition(ob, S, a, b):
		for i in range(1, len(S)):
			if not int(S[:i]) % a:
				if not int(S[i:]) % b:
					return S[:i] + ' ' + S[i:]
		return -1
