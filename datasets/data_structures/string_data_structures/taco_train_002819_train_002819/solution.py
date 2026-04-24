def makeList(a):
	l = len(a)
	if l == 0:
		head = node()
		head.data = 'EMPTY'
		return head
	head = node()
	head.data = a[0]
	head.left = None
	p = head
	for i in range(1, l):
		p.right = node()
		p.right.data = a[i]
		p.right.left = p
		p = p.right
	return head

class Solution:

	def mailDesign(self, N, Q, query):
		if N == 1:
			unread = [1]
		else:
			unread = [i for i in range(1, N + 1)]
		read = []
		trash = []
		for i in range(0, Q * 2, 2):
			m = query[i]
			x = query[i + 1]
			if m == 1:
				unread.remove(x)
				read.append(x)
			elif m == 2:
				read.remove(x)
				trash.append(x)
			elif m == 3:
				unread.remove(x)
				trash.append(x)
			else:
				trash.remove(x)
				read.append(x)
		x = makeList(unread)
		y = makeList(read)
		z = makeList(trash)
		return [x, y, z]
