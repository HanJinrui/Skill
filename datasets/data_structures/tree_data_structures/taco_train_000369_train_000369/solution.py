import math

def diff(root, res):
	if root is None:
		return (math.inf, res)
	if not root.left and (not root.right):
		return (root.data, res)
	(min_left, res) = diff(root.left, res)
	(min_right, res) = diff(root.right, res)
	min_node = min(min_left, min_right)
	res = max(res, root.data - min_node)
	return (min(min_node, root.data), res)

def maxDiff(root):
	res = -math.inf
	(_, res) = diff(root, res)
	return res
