class Solution:

	def zigZagTraversal(self, root):
		q = [root]
		result = []
		level = 1
		while q:
			lst = []
			size = len(q)
			for i in range(size):
				ele = q.pop(0)
				lst.append(ele.data)
				if ele.left != None:
					q.append(ele.left)
				if ele.right != None:
					q.append(ele.right)
			if level % 2 == 0:
				result.extend(lst[::-1])
			else:
				result.extend(lst)
			level += 1
		return result
