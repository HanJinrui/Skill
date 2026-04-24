class Solution:

	def printPairs(self, arr, n, k):

		def find(N):
			res = []
			p = 1
			while p * p <= N:
				if N % p == 0:
					res.append(p)
					if N // p != p:
						res.append(N // p)
				p += 1
			return res
		ans = 0
		uset = set()
		for a in arr:
			uset.add(a)
		for i in range(n):
			if k in uset and k < arr[i]:
				ans += 1
			if arr[i] >= k:
				a = arr[i]
				divs = find(a - k)
				for b in divs:
					if b in uset and a % b == k and (a != b):
						ans += 1
		return ans
