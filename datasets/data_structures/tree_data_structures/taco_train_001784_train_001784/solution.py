def serialize(root, A):
	if not root:
		A.append('#')
		return A
	A.append(root.data)
	serialize(root.left, A)
	serialize(root.right, A)
	return A

def deSerialize(A):
	c = A.pop(0)
	if c == '#':
		return None
	r = Node(c)
	r.left = deSerialize(A)
	r.right = deSerialize(A)
	return r
