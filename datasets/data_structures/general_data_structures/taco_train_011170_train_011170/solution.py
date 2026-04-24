from typing import List

class Solution:

	def subarrayRanges(self, N: int, arr) -> int:
		res = 0
		inc = []
		dec = []
		for i in range(N + 1):
			while inc and (i == N or arr[inc[-1]] < arr[i]):
				curIndex = inc.pop()
				left = inc[-1] if inc else -1
				right = i
				res += (curIndex - left) * (right - curIndex) * arr[curIndex]
			while dec and (i == N or arr[dec[-1]] > arr[i]):
				curIndex = dec.pop()
				left = dec[-1] if dec else -1
				right = i
				res -= (curIndex - left) * (right - curIndex) * arr[curIndex]
			inc.append(i)
			dec.append(i)
		return res
