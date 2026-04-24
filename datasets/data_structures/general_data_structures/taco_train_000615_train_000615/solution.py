from itertools import product

class RangeQuery(object):

	def __init__(self, items, fn):
		self._rq = rq = {(i, 0): item for (i, item) in enumerate(items)}
		self._fn = fn
		n = len(items)
		for (step, i) in product(range(1, n.bit_length()), range(n)):
			j = i + 2 ** (step - 1)
			if j < n:
				rq[i, step] = fn(rq[i, step - 1], rq[j, step - 1])
			else:
				rq[i, step] = rq[i, step - 1]

	def query(self, start, stop):
		j = (stop - start).bit_length() - 1
		x = self._rq[start, j]
		y = self._rq[stop - 2 ** j, j]
		return self._fn(x, y)

def split_segment(start, end, x):
	prev_under = True
	splits = []
	this_under = False
	for i in range(start, end + 1):
		this_under = a[i] <= x
		if this_under != prev_under:
			splits.append(i - int(this_under))
			prev_under = this_under
	if not this_under:
		splits.append(end)
	parts = [[splits[i], splits[i + 1]] for i in range(0, len(splits) - 1, 2)]
	return parts
(n, q) = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
extras = int((len(a) - n) / 3)
querries = [map(int, input().split(' ')) for qi in range(q - extras)]
for ei in range(extras):
	querries.insert(0, a[-3:])
	a = a[:-3]
rqmax = RangeQuery(a, max)
for qi in range(q):
	(l, r, x) = querries[qi]
	ugly = 0
	segcount = int((r - l + 1) * (r - l + 2) / 2)
	if rqmax.query(l - 1, r) <= x:
		print(segcount)
		continue
	splits = split_segment(l - 1, r - 1, x)
	for (sl, sr) in splits:
		if sl == sr:
			ugly += 1
			continue
		for li in range(sl, sr + 1):
			result = a[li]
			for ri in range(li, sr + 1):
				result &= a[ri]
				if result > x:
					ugly += 1
				else:
					break
	print(segcount - ugly)
