class Solution:

	def huffmanCodes(self, s, f, N):

		class Node:

			def __init__(self, data, lc=None, rc=None):
				(self.d, self.lc, self.rc) = (data, lc, rc)

			def __lt__(self, n):
				return self.d[0] < n.d[0]
		h = [Node(data=(f[i], s[i])) for i in range(N)]
		import heapq
		heapq.heapify(h)
		while len(h) > 1:
			(n1, n2) = (heapq.heappop(h), heapq.heappop(h))
			heapq.heappush(h, Node(data=(n1.d[0] + n2.d[0], -1), lc=n1, rc=n2))
		root = heapq.heappop(h)
		res = []

		def pre(root, path):
			if root:
				pre(root.lc, path + '0')
				pre(root.rc, path + '1')
				if not root.lc and (not root.rc):
					res.append(path)
		pre(root, '')
		return res
