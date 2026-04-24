from math import log
(h, w) = map(int, input().split())
ff = 2 ** int(log(h) / log(2))
ss = 2 ** int(log(w) / log(2))
if ff > ss:
	ff = min(ff, int(ss * 1.25))
else:
	ss = min(ss, int(ff * 1.25))
ff2 = min(int(ss * 1.25), h)
ss2 = min(int(ff * 1.25), w)
if ff * ss2 > ss * ff2:
	print(ff, ss2)
else:
	print(ff2, ss)
