class Solution:

	def canConstruct(self, ransomNote, magazine):
		return all((ransomNote.count(i) <= magazine.count(i) for i in set(ransomNote)))
