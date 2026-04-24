class Solution:

	def jugglerSequence(self, N):
		seq = [N]
		while N > 1:
			if N % 2 == 0:
				N = int(N ** 0.5)
			else:
				N = int(N ** 1.5)
			seq.append(N)
		return seq
