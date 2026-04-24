def printNumber(s, n):
	sr = 'abcdefghijklmnopqrstuvwxyz'
	nr = '22233344455566677778889999'
	a = ''
	for i in s:
		a += nr[sr.index(i)]
	return a
