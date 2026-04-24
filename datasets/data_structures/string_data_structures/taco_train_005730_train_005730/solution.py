class Solution:

	def nextGreatestLetter(self, letters, target):
		for char in letters:
			if char > target:
				return char
		return letters[0]
