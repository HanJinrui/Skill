class Solution:

	def commonSubseq(ob, S1, S2):
		return int(bool(set(S1).intersection(set(S2))))
