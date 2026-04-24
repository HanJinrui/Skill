class Solution:

	def maxPalindrome(self, head):
		a = []
		c = head
		while c:
			a.append(c.data)
			c = c.next
		l = 1
		for i in range(len(a)):
			for j in range(i + 1, len(a) + 1):
				if a[i:j] == a[i:j][::-1]:
					l = max(l, j - i)
		return l
