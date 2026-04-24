class Solution:

	def minStepToReachTarget(self, pos, target, n):
		q = [(pos[0], pos[1], 0)]
		dirn = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
		vis = set([(pos[0], pos[1])])
		while q:
			(x, y, d) = q.pop(0)
			if [x, y] == target:
				return d
			for (dx, dy) in dirn:
				if 0 < x + dx <= n and 0 < y + dy <= n and ((x + dx, y + dy) not in vis):
					q.append((x + dx, y + dy, d + 1))
					vis.add((x + dx, y + dy))
