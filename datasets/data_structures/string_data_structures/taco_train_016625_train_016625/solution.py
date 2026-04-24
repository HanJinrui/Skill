class Solution:

	def modify(self, s):
		vowels = 'aeiou'
		stack = [c for c in s if c in vowels]
		return ''.join((stack.pop() if c in vowels else c for c in s))
