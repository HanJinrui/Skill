import os
import sys
from io import BytesIO, IOBase
from types import GeneratorType
from collections import defaultdict
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
sys.setrecursionlimit(2 * 10 ** 5)

def bootstrap(f, stack=[]):

	def wrappedfunc(*args, **kwargs):
		if stack:
			return f(*args, **kwargs)
		else:
			to = f(*args, **kwargs)
			while True:
				if type(to) is GeneratorType:
					stack.append(to)
					to = next(to)
				else:
					stack.pop()
					if not stack:
						break
					to = stack[-1].send(to)
			return to
	return wrappedfunc

@bootstrap
def dfs(u, p):
	for j in adj[u]:
		if j != p:
			yield dfs(j, u)
			if d[j, u] != 0:
				ways[u] += ways[j] + 1
	yield

@bootstrap
def dfs2(u, p, v):
	for j in adj[u]:
		if j != p:
			if d[u, j] == 0:
				yield dfs2(j, u, 0)
			else:
				yield dfs2(j, u, v + ways[u] - ways[j])
	ans[u] = ways[u] * (ways[u] - 1) + v * (v - 1) + 2 * (ways[u] * v + (ways[u] + v) * (n - 1 - ways[u] - v))
	yield

def val(n):
	for j in str(n):
		if j == '4' or j == '7':
			pass
		else:
			return 1
	return 0
n = int(input())
adj = [[] for i in range(n + 1)]
d = dict()
for j in range(n - 1):
	c = list(map(int, input().split()))
	adj[c[0]].append(c[1])
	adj[c[1]].append(c[0])
	c[2] = val(c[2])
	d[c[0], c[1]] = c[2]
	d[c[1], c[0]] = c[2]
ways = [0] * (n + 1)
dfs(1, 0)
ans = [0] * (n + 1)
dfs2(1, 0, 0)
print(n * (n - 1) * (n - 2) - sum(ans))
