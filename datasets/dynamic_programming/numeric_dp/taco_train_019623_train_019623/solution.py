class Solution:

	def countNumberswith4(self, N):
		list1 = [i for i in range(1, N + 1) if '4' in str(i)]
		return len(list1)
