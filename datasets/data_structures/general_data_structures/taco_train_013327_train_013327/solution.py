import math
import os
import random
import re
import sys
mod = 1000000007
polys = [1]
maxLen = 100

class Node:

	def __init__(self, l, r):
		self.l = l
		self.r = r
		self.off = 0
		if r - l < maxLen:
			self.left = self.right = None
		else:
			mid = r + l >> 1
			self.left = Node(self.l, mid)
			self.right = Node(mid, self.r)
		self.mask = None

	def add(self, l, r, off):
		if self.r < l or r < self.l:
			return
		l = max(l, self.l)
		r = min(r, self.r)
		if l == r or off == 0:
			return
		if l == self.l and r == self.r and (self.left is not None):
			self.off += off
			self.off %= 26
		elif self.left is None:
			if off % 26 > 0 and (l > 0 or len(arr) != r):
				for i in range(l, r):
					arr[i] = (arr[i] + off) % 26
			self.mask = None
		else:
			self.left.add(l, r, off)
			self.right.add(l, r, off)

		def countPolyndroms(self, l, r):
			mask = self.getMask(l, r)
			counter = sum(mask)
			deg = r - l - counter
			while len(polys) <= deg:
				polys.append(polys[-1] * 2 % mod)
			res = (counter + 1) * polys[deg] - 1
			return res % mod

	def getMask(self, l, r):
		if self.r < l or r < self.l:
			return [0] * 26
		l = max(l, self.l)
		r = min(r, self.r)
		if self.left:
			lmask = self.left.getMask(l, r)
			if all(lmask):
				return lmask
			rmask = self.right.getMask(l, r)
			if all(rmask):
				return rmask
			res = [0] * 26
			for i in range(26):
				res[(i + self.off) % 26] = rmask[i] or lmask[i]
			return res
		if self.l == l and self.r == r:
			if self.mask is None:
				self.mask = [0] * 26
				for i in range(l, r):
					self.mask[arr[i]] = 1
			if self.off:
				res = [0] * 26
				for i in range(26):
					res[(i + self.off) % 26] = self.mask[i]
			else:
				res = self.mask
			return res
		mask = [0] * 26
		for i in range(l, r):
			mask[arr[i]] = 1
		return mask
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
q = int(first_multiple_input[1])
arr = [ord(c) - 97 for c in input()]
root = Node(0, len(arr))
for _ in range(q):
	qu = input().strip().split()
	l = int(qu[1])
	r = int(qu[2]) + 1
	if qu[0] == '1':
		t = int(qu[3])
		root.add(l, r, t)
	else:
		counter = sum(root.getMask(l, r))
		deg = r - l - counter
		while len(polys) <= deg:
			polys.append(polys[-1] * 2 % mod)
		print(((counter + 1) * polys[deg] - 1) % mod)
