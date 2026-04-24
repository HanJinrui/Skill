def maxlength(s):
	a = s.split('0')
	a.sort(reverse=True)
	return len(a[0])
