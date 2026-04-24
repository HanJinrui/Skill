class Solution:

	def isCompleteBT(self, root):
		q = [root]
		i = 0
		while q[i]:
			q.append(q[i].left)
			q.append(q[i].right)
			i += 1
		return not any(q[i:])
