import collections

def isCousin(root, a, b):
	[d1, p1] = dfs(root, a) or [None, None]
	[d2, p2] = dfs(root, b) or [None, None]
	return d1 == d2 and p1 != p2

def dfs(n, a, p=None, d=0):
	if not n:
		return None
	if n.data == a:
		return [d, p]
	return dfs(n.left, a, n, d + 1) or dfs(n.right, a, n, d + 1)
