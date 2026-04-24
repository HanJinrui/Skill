class Solution:

	def smallestSubsegment(self, arr, n):
		d = {}
		for i in range(n):
			if arr[i] in d:
				d[arr[i]].append(i)
			else:
				d[arr[i]] = [i]
		l = [len(d[i]) for i in d]
		a = max(l)
		t = []
		for i in d:
			if len(d[i]) == a:
				t.append(d[i])
		w = []
		for i in t:
			q = i[-1] - i[0]
			w.append([q, i])
		w.sort()
		p = w[0][1][0]
		r = w[0][1][-1]
		return arr[p:r + 1]
