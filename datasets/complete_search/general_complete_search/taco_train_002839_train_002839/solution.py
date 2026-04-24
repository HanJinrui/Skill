n = int(input())
ans = (-10 ** 8, ['Impossible'])
s = []
d = {}
fl = True
a = [list(map(int, input().split())) for i in range(n)]

def job(nom, l, m, w):
	global s, ans
	if nom == n // 2 and fl:
		(su, ss) = d.get((m - l, w - l), (-10 ** 10, []))
		if l > su:
			d[m - l, w - l] = (l, s[:])
		return
	if nom == n:
		(su, ss) = d.get((l - m, l - w), (-10 ** 9, []))
		if su + l > ans[0]:
			ans = (su + l, ss[:] + s[:])
		return
	s += ['MW']
	job(nom + 1, l, m + a[nom][1], w + a[nom][2])
	s[-1] = 'LW'
	job(nom + 1, l + a[nom][0], m, w + a[nom][2])
	s[-1] = 'LM'
	job(nom + 1, l + a[nom][0], m + a[nom][1], w)
	s.pop()
job(0, 0, 0, 0)
fl = False
if n == 1:
	d[0, 0] = (0, [])
job(n // 2, 0, 0, 0)
print('\n'.join(ans[1]))
