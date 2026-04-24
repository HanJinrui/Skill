class Solution:

	def splitList(self, h, h1, h2):
		f = h
		c = 1
		h1 = h2 = t = h
		while f.next != h:
			f = f.next
			c += 1
		if c % 2 == 0:
			c = c // 2
		else:
			c = c // 2 + 1
		while c != 0:
			t = h2
			h2 = h2.next
			c -= 1
		t.next = h1
		f.next = h2
		return (h1, h2)
