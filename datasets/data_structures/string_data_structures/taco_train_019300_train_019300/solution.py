class Solution:

	def generate_binary_string(self, s):
		l = []
		q = [s]
		while q:
			cur = q.pop(0)
			if '?' in cur:
				q.append(cur.replace('?', '0', 1))
				q.append(cur.replace('?', '1', 1))
			else:
				l.append(cur)
		return l
