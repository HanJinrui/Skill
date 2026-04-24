for _ in range(int(input())):
	(a, b) = map(int, input().split())
	(c, d) = map(int, input().split())
	w = ''
	for i in range(a):
		x = list(input())
		if x.count('F') >= c or (x.count('F') == c - 1 and x.count('P') >= d):
			w += '1'
		else:
			w += '0'
	print(w)
