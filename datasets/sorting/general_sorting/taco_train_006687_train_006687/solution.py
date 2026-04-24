import bisect

class Solution:

	def findMaxGuests(self, Entry, Exit, N):
		Entry.sort()
		Exit.sort()
		mx = 0
		for i in range(N):
			x = bisect.bisect(Entry, Exit[i])
			if x - i > mx:
				mx = x - i
				time = Entry[x - 1]
		return [mx, time]
