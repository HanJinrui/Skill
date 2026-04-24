class Solution:

	def getCrazy(self, S):
		ans = S[0]
		for j in range(1, len(S)):
			if ans[-1].islower():
				ans += S[j].upper()
			else:
				ans += S[j].lower()
		return ans
