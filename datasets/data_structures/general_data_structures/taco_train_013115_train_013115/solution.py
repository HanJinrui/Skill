class Solution:

	def findSpecialInteger(self, arr: List[int]) -> int:
		return max(set(arr), key=arr.count)
