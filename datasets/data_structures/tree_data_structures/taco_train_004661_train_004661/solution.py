def buildTree(In, post, n):
	if In:
		index = In.index(post.pop())
		root = Node(In[index])
		root.right = buildTree(In[index + 1:], post, n)
		root.left = buildTree(In[:index], post, n)
		return root
