class Solution:

	def maximumMeetings(self, n, start, end):
		count = 1
		l = sorted(zip(end, start))
		limit = l[0][0]
		for x in range(1, n):
			if l[x][1] > limit:
				count += 1
				limit = l[x][0]
		return count
