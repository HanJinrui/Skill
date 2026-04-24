import os
import sys
from io import BytesIO, IOBase

def main():
	t = int(input())
	for _ in range(t):
		if _ != 0:
			input()
		h = int(input())
		l1 = list(map(int, input().split()))
		v = int(input())
		l2 = list(map(int, input().split()))
		hKnap = [1]
		vKnap = [1]
		if h != v or sum(l1) % 2 != 0 or sum(l2) % 2 != 0:
			print('No')
			continue
		for elem in l1:
			hKnap.append(hKnap[-1] << elem | hKnap[-1])
		for elem in l2:
			vKnap.append(vKnap[-1] << elem | vKnap[-1])
		hSet = []
		hSet2 = []
		vSet = []
		vSet2 = []
		if hKnap[-1] & 1 << sum(l1) // 2:
			curSum = sum(l1) // 2
			for i in range(h - 1, -1, -1):
				if curSum >= l1[i] and hKnap[i] & 1 << curSum - l1[i]:
					curSum -= l1[i]
					hSet.append(l1[i])
				else:
					hSet2.append(l1[i])
		if vKnap[-1] & 1 << sum(l2) // 2:
			curSum = sum(l2) // 2
			for i in range(v - 1, -1, -1):
				if curSum >= l2[i] and vKnap[i] & 1 << curSum - l2[i]:
					curSum -= l2[i]
					vSet.append(l2[i])
				else:
					vSet2.append(l2[i])
		if not hSet or not vSet:
			print('No')
		else:
			print('Yes')
			if len(hSet) < len(hSet2):
				hTupleS = tuple(sorted(hSet))
				hTupleL = tuple(sorted(hSet2))
			else:
				hTupleS = tuple(sorted(hSet2))
				hTupleL = tuple(sorted(hSet))
			if len(vSet) < len(vSet2):
				vTupleS = tuple(sorted(vSet))
				vTupleL = tuple(sorted(vSet2))
			else:
				vTupleS = tuple(sorted(vSet2))
				vTupleL = tuple(sorted(vSet))
			currentLoc = [0, 0]
			isHS = True
			isHL = False
			isVS = False
			isVL = True
			hIndex = len(hTupleS) - 1
			vIndex = 0
			for i in range(h):
				if isHS:
					currentLoc[0] += hTupleS[hIndex]
					hIndex -= 1
					if hIndex < 0:
						hIndex = len(hTupleL) - 1
						isHS = False
						isHL = True
				elif isHL:
					currentLoc[0] -= hTupleL[hIndex]
					hIndex -= 1
				print(str(currentLoc[0]) + ' ' + str(currentLoc[1]))
				if isVL:
					currentLoc[1] += vTupleL[vIndex]
					vIndex += 1
					if vIndex >= len(vTupleL):
						vIndex = 0
						isVL = False
						isVH = True
				elif isHL:
					currentLoc[1] -= vTupleS[vIndex]
					vIndex += 1
				print(str(currentLoc[0]) + ' ' + str(currentLoc[1]))
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
