class Solution:

	def FirstNonRepeating(self, A):
		l = []
		mp = {}
		ans = ''
		for i in A:
			if i not in mp:
				l.append(i)
				mp[i] = 1
			elif i in l:
				l.remove(i)
			ans += l[0] if l else '#'
		return ans
