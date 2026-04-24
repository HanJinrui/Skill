class Solution:

	def updateString(self, S):
		noise = ''
		output = ''
		i = 0
		j = 0
		while i < len(S):
			if S[i:i + 3] == 'ada':
				output += S[j:i]
				j = i
				i += 3
				while S[i:i + 2] == 'da':
					i += 2
				noise += S[j:i]
				j = i
			else:
				i += 1
		output += S[j:i]
		return output + noise
