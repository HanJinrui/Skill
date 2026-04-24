class Solution:

	def displayContacts(self, n, contact, s):
		t = []
		for i in range(1, len(s) + 1):
			c = []
			for j in sorted(set(contact)):
				if j.startswith(s[:i]):
					c.append(j)
			if c == []:
				t.append([0])
			else:
				t.append(c)
		return t
