class Solution:

	def pageFaults(self, n, c, pages):
		arr = []
		ans = 0
		for page in pages:
			try:
				arr.remove(page)
			except:
				ans += 1
				if len(arr) == c:
					arr.pop(0)
			finally:
				arr.append(page)
		return ans
