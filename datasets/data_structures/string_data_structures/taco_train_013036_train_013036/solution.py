from collections import Counter
import heapq

class Solution:

	def rearrangeString(self, string):
		ans = ''
		heap = []
		hmap = Counter(string)
		for (x, y) in hmap.items():
			heapq.heappush(heap, [-y, x])
		prev = None
		while heap:
			(f, ch) = heapq.heappop(heap)
			f *= -1
			ans += ch
			if prev != None and prev[0] != 0:
				heapq.heappush(heap, prev)
			prev = [-(f - 1), ch]
		return ans
