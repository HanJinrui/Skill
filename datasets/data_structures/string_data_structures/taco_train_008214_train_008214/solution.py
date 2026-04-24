class Solution:

	def shortestPath(self, s):
		temp = []
		dir_ref = {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'}
		for i in s:
			if dir_ref[i] in temp:
				temp.remove(dir_ref[i])
			else:
				temp.append(i)
		temp = ''.join(sorted(temp))
		return ''.join(sorted(temp))
