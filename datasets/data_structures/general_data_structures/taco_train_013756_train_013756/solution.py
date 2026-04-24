class Solution:

	def arrangeCV(self, head):
		v = ''
		c = ''
		x = 'aeiou'
		while head:
			a = head.data
			if a in x:
				v += a
			else:
				c += a
			head = head.next
		ans = v + c
		for i in ans:
			print(i, end=' ')
