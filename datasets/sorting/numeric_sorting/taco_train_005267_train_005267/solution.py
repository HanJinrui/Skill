import os
from io import BytesIO, IOBase
import sys
from collections import Counter
from math import sqrt, pi, ceil, log, inf, gcd, floor

def main():
	(n, m) = map(int, input().split())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	z = ceil(sqrt(max(max(a), max(b))))
	p = [1] * (z + 1)
	i = 2
	while i * i <= z:
		if p[i] == 1:
			j = i * i
			while j <= z:
				p[j] = 0
				j += i
		i += 1
	pr = []
	for i in range(2, z + 1):
		if p[i]:
			pr.append(i)
	f = Counter()
	f1 = Counter()
	c = [[] for i in range(n)]
	d = [[] for i in range(m)]
	for (i, v) in enumerate(a):
		(y, z) = (ceil(sqrt(v)), v)
		for j in pr:
			if j > y:
				break
			x = 0
			while z % j == 0:
				f[j] += 1
				x += 1
				z = z // j
			if x:
				c[i].append([j, x])
		if z > 1:
			c[i].append([z, 1])
			f[z] += 1
	for (i, v) in enumerate(b):
		(y, z) = (ceil(sqrt(v)), v)
		for j in pr:
			if j > y:
				break
			x = 0
			while z % j == 0:
				f1[j] += 1
				x += 1
				z = z // j
			if x:
				d[i].append([j, x])
		if z > 1:
			d[i].append([z, 1])
			f1[z] += 1
	e = []
	for i in f:
		(f[i], f1[i]) = (max(f[i] - f1[i], 0), max(f1[i] - f[i], 0))
		if f[i] == 0:
			e.append(i)
		if f1[i] == 0:
			del f1[i]
	for i in e:
		del f[i]
	e.clear()
	a = [1] * n
	b = [1] * m
	for i in range(n):
		(z, f2) = (1, 0)
		for j in range(len(c[i])):
			xx = c[i][j][0]
			y = min(c[i][j][1], f[xx])
			z = z * pow(xx, y)
			f[xx] -= y
			if f[xx] == 0:
				del f[xx]
			if len(f) == 0:
				f2 = 1
				break
		a[i] = z
		if f2:
			break
	for i in range(m):
		(z, f2) = (1, 0)
		for j in range(len(d[i])):
			xx = d[i][j][0]
			y = min(d[i][j][1], f1[xx])
			z = z * pow(xx, y)
			f1[xx] -= y
			if f1[xx] == 0:
				del f1[xx]
			if len(f1) == 0:
				f2 = 1
				break
		b[i] = z
		if f2:
			break
	print(n, m)
	print(*a)
	print(*b)
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
(sys.stdin, sys.stdout) = (IOWrapper(sys.stdin), IOWrapper(sys.stdout))
input = lambda : sys.stdin.readline().rstrip('\r\n')
main()
