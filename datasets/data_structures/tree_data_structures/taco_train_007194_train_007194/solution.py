from collections import *

class Solution:

	def sum_at_distK(self, root, target, k):
		d = defaultdict(list)
		q = deque([root])
		while q:
			s = q.popleft()
			if s.left:
				d[s.data].append(s.left.data)
				d[s.left.data].append(s.data)
				q.append(s.left)
			if s.right:
				d[s.data].append(s.right.data)
				d[s.right.data].append(s.data)
				q.append(s.right)
		q = deque()
		q.append([target, 0, -1])
		vis = set()
		ans = 0
		vis.add(target)
		while q:
			(s, dist, par) = q.popleft()
			ans += s
			if dist == k:
				continue
			for j in d[s]:
				if j not in vis:
					q.append([j, dist + 1, s])
					vis.add(j)
		return ans
