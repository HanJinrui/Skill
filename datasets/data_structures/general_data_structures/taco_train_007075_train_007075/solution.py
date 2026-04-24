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
(sys.stdin, sys.stdout) = (IOWrapper(sys.stdin), IOWrapper(sys.stdout))
input = lambda : sys.stdin.readline().rstrip('\r\n')

class query:
	global z

	def __init__(self, l, r, i):
		self.lb = (l - 1) // z
		self.l = l
		self.r = r
		self.ind = i

	def __lt__(a, b):
		return a.lb < b.lb or (a.lb == b.lb and a.r < b.r)
(n, m) = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
	if a[i] > n:
		a[i] = -1
l1 = []
z = int(n ** 0.5)
for i in range(m):
	(x, y) = map(int, input().split())
	l1.append(query(x, y, i))
l1.sort()
d = [0] * (n + 2)
l = 1
r = 0
ans = 0
fans = [0] * m
for i in l1:
	while r < i.r:
		r += 1
		if d[a[r - 1]] == a[r - 1]:
			ans -= 1
		d[a[r - 1]] += 1
		if d[a[r - 1]] == a[r - 1]:
			ans += 1
	while l > i.l:
		l -= 1
		if d[a[l - 1]] == a[l - 1]:
			ans -= 1
		d[a[l - 1]] += 1
		if d[a[l - 1]] == a[l - 1]:
			ans += 1
	while l < i.l:
		if d[a[l - 1]] == a[l - 1]:
			ans -= 1
		d[a[l - 1]] -= 1
		if d[a[l - 1]] == a[l - 1]:
			ans += 1
		l += 1
	while r > i.r:
		if d[a[r - 1]] == a[r - 1]:
			ans -= 1
		d[a[r - 1]] -= 1
		if d[a[r - 1]] == a[r - 1]:
			ans += 1
		r -= 1
	fans[i.ind] = ans
for i in fans:
	print(i)
