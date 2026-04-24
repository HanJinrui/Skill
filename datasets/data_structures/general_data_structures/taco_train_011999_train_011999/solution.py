import os
import sys
from io import BytesIO, IOBase
BUFSIZE = 8192

class FastIO(IOBase):
	newlines = 0

	def __init__(self, file):
		self._fd = file.fileno()
		self.buffer = BytesIO()
		self.writable = 'x' in file.mode or 'r' not in file.mode
		self.write = self.buffer.write if self.writable else None

	def read(self):
		while True:
			b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
			if not b:
				break
			ptr = self.buffer.tell()
			(self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr))
		self.newlines = 0
		return self.buffer.read()

	def readline(self):
		while self.newlines == 0:
			b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
			self.newlines = b.count(b'\n') + (not b)
			ptr = self.buffer.tell()
			(self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr))
		self.newlines -= 1
		return self.buffer.readline()

	def flush(self):
		if self.writable:
			os.write(self._fd, self.buffer.getvalue())
			(self.buffer.truncate(0), self.buffer.seek(0))

class IOWrapper(IOBase):

	def __init__(self, file):
		self.buffer = FastIO(file)
		self.flush = self.buffer.flush
		self.writable = self.buffer.writable
		self.write = lambda s: self.buffer.write(s.encode('ascii'))
		self.read = lambda : self.buffer.read().decode('ascii')
		self.readline = lambda : self.buffer.readline().decode('ascii')

def inp():
	return sys.stdin.readline().rstrip()

def mpint():
	return map(int, inp().split(' '))

def itg():
	return int(inp())

class LazySegmentTree:

	def __init__(self, data, default=0, func=max):
		self._default = default
		self._func = func
		self._len = len(data)
		self._size = _size = 1 << (self._len - 1).bit_length()
		self._lazy = [0] * (2 * _size)
		self.data = [default] * (2 * _size)
		self.data[_size:_size + self._len] = data
		for i in reversed(range(_size)):
			self.data[i] = func(self.data[i + i], self.data[i + i + 1])

	def __len__(self):
		return self._len

	def _push(self, idx):
		(q, self._lazy[idx]) = (self._lazy[idx], 0)
		self._lazy[2 * idx] += q
		self._lazy[2 * idx + 1] += q
		self.data[2 * idx] += q
		self.data[2 * idx + 1] += q

	def _update(self, idx):
		for i in reversed(range(1, idx.bit_length())):
			self._push(idx >> i)

	def _build(self, idx):
		idx >>= 1
		while idx:
			self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1]) + self._lazy[idx]
			idx >>= 1

	def add(self, start, stop, value):
		start = start_copy = start + self._size
		stop = stop_copy = stop + self._size
		while start < stop:
			if start & 1:
				self._lazy[start] += value
				self.data[start] += value
				start += 1
			if stop & 1:
				stop -= 1
				self._lazy[stop] += value
				self.data[stop] += value
			start >>= 1
			stop >>= 1
		self._build(start_copy)
		self._build(stop_copy - 1)

	def query(self, start, stop, default=None):
		start += self._size
		stop += self._size
		self._update(start)
		self._update(stop - 1)
		res = self._default if default is None else default
		while start < stop:
			if start & 1:
				res = self._func(res, self.data[start])
				start += 1
			if stop & 1:
				stop -= 1
				res = self._func(res, self.data[stop])
			start >>= 1
			stop >>= 1
		return res

	def __repr__(self):
		return 'LazySegmentTree({})'.format(list(map(lambda i: self.query(i, i + 1), range(self._len))))

class SweepLine:

	def __init__(self, data=None, inclusive=True):
		if data:
			self.data = [(*pair, i) for (i, pair) in enumerate(data)]
		else:
			self.data = []
		self.discrete_dict = self.restore = None
		self.INCLUSIVE = inclusive

	def add_rectangle(self, rectangle):
		self.data.append((*rectangle, len(self.data)))

	def _discrete(self):
		st = set()
		operations = []
		for (p1, p2, i) in self.data:
			st |= {*p1, *p2}
			operations.append((p1[1], -1, p1[0], p2[0], i))
			operations.append((p2[1], 1, p1[0], p2[0], i))
		self.restore = sorted(st)
		self.discrete_dict = dict(zip(self.restore, range(len(st))))
		self.operations = sorted(operations)

	def max_intersect(self, get_points=False):
		if not self.restore:
			self._discrete()
		d = self.discrete_dict
		tree = LazySegmentTree([0] * len(self.restore))
		result = (0, None)
		for (y, v, left, right, i) in self.operations:
			(left, right, v) = (d[left], d[right], -v)
			tree.add(left, right + self.INCLUSIVE, v)
			if v == 1:
				intersect = tree.query(left, right + self.INCLUSIVE)
				if intersect > result[0]:
					result = (intersect, i)
		tree = LazySegmentTree([0] * len(self.restore))
		if get_points:
			for (y, v, left, right, i) in self.operations:
				(left, right, v) = (d[left], d[right], -v)
				tree.add(left, right + self.INCLUSIVE, v)
				if i == result[1]:
					for lf in range(left, right + self.INCLUSIVE):
						if tree.query(lf, lf + 1) == result[0]:
							return (result[0], i, self.restore[lf])
		return result

def main():
	n = itg()
	data = []
	for _ in range(n):
		(lf, md, rg) = mpint()
		data.append(((lf, md), (md, rg)))
	sweep = SweepLine(data)
	(ans1, idx, left) = sweep.max_intersect(True)
	right = data[idx][0][1]
	print(ans1)
	ans2 = []
	for (i, pair) in enumerate(data):
		(lf, md, rg) = (pair[0][0], pair[0][1], pair[1][1])
		if lf <= left <= md <= right <= rg:
			ans2.append(i + 1)
	if len(ans2) != ans1:
		print(AssertionError, len(ans2))
	else:
		print(*ans2)
DEBUG = 0
URL = 'https://codeforces.com/contest/377/problem/D'
if DEBUG == 1:
	import requests
	from ACgenerator.Y_Test_Case_Runner import TestCaseRunner
	runner = TestCaseRunner(main, URL)
	inp = runner.input_stream
	print = runner.output_stream
	runner.checking()
else:
	if DEBUG != 3:
		(sys.stdin, sys.stdout) = (IOWrapper(sys.stdin), IOWrapper(sys.stdout))
	if DEBUG:
		_print = print

		def print(*args, **kwargs):
			_print(*args, **kwargs)
			sys.stdout.flush()
	main()
