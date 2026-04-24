n = int(input())
mn = [float('inf')] * 256
ans = ''
done = set()

def gen(vals, st):
	global mn, ans
	if '|'.join([str(x) for x in vals]) in done:
		return
	done.add('|'.join([str(x) for x in vals]))
	if vals[-1] == n:
		if len(vals) < mn[n]:
			mn[n] = len(vals)
			ans = st
		return
	if len(vals) > 5:
		return
	for i in range(len(vals)):
		for z in [8, 4, 2, 1]:
			e = vals[i] * z
			if e > n:
				continue
			if e > vals[-1]:
				nw = 'e' + chr(ord('a') + len(vals)) + 'x'
				I = 'e' + chr(ord('a') + i) + 'x'
				gen(vals + [e], st + 'lea ' + nw + ', [' + str(z) + '*' + I + ']\n')
		for j in range(len(vals)):
			for z in [8, 4, 2, 1]:
				e = vals[i] + z * vals[j]
				if e > n:
					continue
				if e > vals[-1]:
					nw = 'e' + chr(ord('a') + len(vals)) + 'x'
					I = 'e' + chr(ord('a') + i) + 'x'
					J = 'e' + chr(ord('a') + j) + 'x'
					gen(vals + [e], st + 'lea ' + nw + ', [' + I + ' + ' + str(z) + '*' + J + ']\n')
gen([1], '')
print(ans.count('\n'))
print(ans, end='')
