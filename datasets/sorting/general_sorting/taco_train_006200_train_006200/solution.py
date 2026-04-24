from sys import stdin, stdout

def ask(l, r):
	stdout.write('? ' + str(l) + ' ' + str(r) + '\n')
	stdout.flush()
	nd = int(stdin.readline())
	return nd
try:
	n = int(stdin.readline())
	l = 1
	r = n
	nd = ask(l, r)
	if nd > 1 and ask(1, nd) == nd:
		l = 1
		r = nd
		while l + 1 != r:
			md = (l + r) // 2
			if ask(md, nd) == nd:
				l = md
			else:
				r = md
		stdout.write('! ' + str(l) + '\n')
	else:
		l = nd
		r = n
		while l + 1 != r:
			md = (l + r) // 2
			if ask(nd, md) == nd:
				r = md
			else:
				l = md
		stdout.write('! ' + str(r) + '\n')
except:
	pass
