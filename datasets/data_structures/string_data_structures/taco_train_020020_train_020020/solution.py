class Solution:

	def printMinNumberForPattern(ob, S):
		st = []
		ans = ''
		for i in range(len(S) + 1):
			st.append(i + 1)
			if i == len(S) or S[i] == 'I':
				while len(st) > 0:
					ans += str(st.pop())
		return ans
