class Solution:

	def LargestSwap(self, S):
		i = -1
		j = len(S) - 1
		mx = S[-1]
		for x in range(len(S) - 2, -1, -1):
			if S[x] < mx:
				i = x
			elif S[x] > mx:
				mx = S[x]
				j = x
		if i == -1:
			return S
		S = list(S)
		(S[i], S[j]) = (S[j], S[i])
		S = ''.join(S)
		return S
