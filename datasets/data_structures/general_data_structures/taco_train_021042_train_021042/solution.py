from typing import List

class Solution:

	def makeBeautiful(self, arr: List[int]) -> List[int]:
		st = []
		for i in arr:
			if not st:
				st.append(i)
				continue
			if st[-1] >= 0 and i < 0 or (st[-1] < 0 and i >= 0):
				st.pop()
			else:
				st.append(i)
		return st
