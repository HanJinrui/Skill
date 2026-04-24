class Solution:

	def mergeKLists(self, arr, K):
		l = []
		for i in arr:
			itr = i
			while itr:
				l.append(itr.data)
				itr = itr.next
		l.sort()
		for i in l:
			print(i, end=' ')
