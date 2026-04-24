import bisect

class Solution:

	def countPairs(self, arr, n):
		srt_arr = []
		count = 0
		for i in range(n):
			arr[i] = i * arr[i]
			index = bisect.bisect(srt_arr, arr[i])
			count += i - index
			srt_arr.insert(index, arr[i])
		return count
