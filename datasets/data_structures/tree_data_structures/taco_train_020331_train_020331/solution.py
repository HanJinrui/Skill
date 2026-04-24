class Solution:

	def largestValues(self, root):
		ans = []
		dfs(root, 0, ans)
		return ans

def dfs(n, l, ans):
	if not n:
		return
	if len(ans) == l:
		ans.append(n.data)
	ans[l] = max(ans[l], n.data)
	dfs(n.left, l + 1, ans)
	dfs(n.right, l + 1, ans)
