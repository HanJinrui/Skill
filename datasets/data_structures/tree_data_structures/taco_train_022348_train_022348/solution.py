class Solution:

	def printCousins(self, root, node_to_find):
		ans = []
		queue = [root]
		flag = 1
		while queue and flag:
			for i in range(len(queue)):
				cur = queue.pop(0)
				if cur.left == node_to_find or cur.right == node_to_find:
					flag = 0
				else:
					if cur.left:
						queue.append(cur.left)
					if cur.right:
						queue.append(cur.right)
		for i in queue:
			ans.append(i.data)
		return ans if ans else [-1]
