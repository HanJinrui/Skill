import time

class Solution:

	def timeGap(self, st, et):
		l1 = st.split(':')
		l2 = et.split(':')
		l1[0] = str(int(l1[0]) * 3600)
		l1[1] = str(int(l1[1]) * 60)
		l2[0] = str(int(l2[0]) * 3600)
		l2[1] = str(int(l2[1]) * 60)
		total_seconds1 = int(l1[0]) + int(l1[1]) + int(l1[2])
		total_seconds2 = int(l2[0]) + int(l2[1]) + int(l2[2])
		total = total_seconds2 - total_seconds1
		res = time.strftime('%H:%M:%S', time.gmtime(total))
		return res
