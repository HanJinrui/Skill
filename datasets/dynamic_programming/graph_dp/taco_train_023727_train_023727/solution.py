import os
import sys
from io import BytesIO, IOBase
_print = print
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
from collections import deque

def solve():
	(d, s) = mpint()
	dp = [[(-1, -1)] * (d + 1) for _ in range(s + 1)]
	dq = deque([(0, 0)])
	while dq:
		(digit_sum, mod) = dq.popleft()
		for dg in range(10):
			dg_sum = digit_sum + dg
			m = (mod * 10 + dg) % d
			if dg_sum <= s and dp[dg_sum][m][0] == -1:
				dp[dg_sum][m] = (dg, mod)
				dq.append((dg_sum, m))
		if dp[s][0][0] != -1:
			break
	if dp[s][0][0] == -1:
		return -1
	ans = []
	d = 0
	while s:
		(dg, d) = dp[s][d]
		s -= dg
		ans.append(chr(dg + 48))
	return ''.join(reversed(ans))

def main():
	print(solve())
DEBUG = 0
URL = 'https://codeforces.com/contest/1070/problem/A'
if DEBUG == 1:
	import requests
	from ACgenerator.Y_Test_Case_Runner import TestCaseRunner
	runner = TestCaseRunner(main, URL)
	inp = runner.input_stream
	print = runner.output_stream
	runner.checking()
else:
	if DEBUG != 2:
		(sys.stdin, sys.stdout) = (IOWrapper(sys.stdin), IOWrapper(sys.stdout))
	if DEBUG:

		def print(*args, **kwargs):
			_print(*args, **kwargs)
			sys.stdout.flush()
	main()
