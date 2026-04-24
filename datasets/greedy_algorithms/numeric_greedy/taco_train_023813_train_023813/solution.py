import sys
from sys import stdout
import os
ii = 0
_inp = b''

def getchar():
	global ii, _inp
	if ii >= len(_inp):
		_inp = os.read(0, 4096)
		ii = 0
	if not _inp:
		return b' '[0]
	ii += 1
	return _inp[ii - 1]

def input():
	c = getchar()
	if c == b'-'[0]:
		x = 0
		sign = 1
	else:
		x = c - b'0'[0]
		sign = 0
	c = getchar()
	while c >= b'0'[0]:
		x = 10 * x + c - b'0'[0]
		c = getchar()
	if c == b'\r'[0]:
		getchar()
	return -x if sign else x

def main():
	n = int(input())
	arr = [-1] * n
	for i in range(1, n):
		print('?', *[i] * (n - 1) + [n])
		sys.stdout.flush()
		k = int(input())
		if k:
			arr[-1] = i
			break
	else:
		arr[-1] = n
	for i in range(1, n + 1):
		if i == arr[-1]:
			continue
		print('?', *[arr[-1]] * (n - 1) + [i])
		sys.stdout.flush()
		k = int(input())
		arr[k - 1] = i
	print('!', *arr)
	sys.stdout.flush()
main()
