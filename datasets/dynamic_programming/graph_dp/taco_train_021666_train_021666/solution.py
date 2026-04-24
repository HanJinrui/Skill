import sys
from array import array
import re

def input():
	return sys.stdin.buffer.readline().decode('utf-8')

class Widget(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y

class Box(object):

	def __init__(self):
		self.children = []
		self.border = 0
		self.spacing = 0
		self._x = -1
		self._y = -1

	def set_border(self, size):
		self.border = size

	def set_spacing(self, size):
		self.spacing = size

	def pack(self, widget):
		self.children.append(widget)

	@property
	def x(self):
		if self._x == -1:
			self._x = max((child.x for child in self.children)) + self.border * 2 if self.children else 0
		return self._x

	@property
	def y(self):
		if self._y == -1:
			self._y = max((child.y for child in self.children)) + self.border * 2 if self.children else 0
		return self._y

class HBox(Box):

	@property
	def x(self):
		if self._x == -1:
			if not self.children:
				return 0
			a = [child.x for child in self.children]
			self._x = self.border * 2 + sum(a) + self.spacing * (len(a) - 1)
		return self._x

class VBox(Box):

	@property
	def y(self):
		if self._y == -1:
			if not self.children:
				return 0
			a = [child.y for child in self.children]
			self._y = self.border * 2 + sum(a) + self.spacing * (len(a) - 1)
		return self._y
n = int(input())
namespace = {}
pattern = re.compile('([^(]+?)\\(([^)]+?)\\)')

def parse(s):
	return re.search(pattern, s).groups()
for _ in range(n):
	command = input().split()
	if command[0] == 'Widget':
		(name, args) = parse(command[1])
		namespace[name] = Widget(*tuple(map(int, args.split(','))))
	elif command[0] == 'VBox':
		namespace[command[1]] = VBox()
	elif command[0] == 'HBox':
		namespace[command[1]] = HBox()
	else:
		(name, method) = command[0].split('.')
		(method, args) = parse(method)
		if method == 'set_border':
			namespace[name].set_border(int(args))
		elif method == 'set_spacing':
			namespace[name].set_spacing(int(args))
		elif method == 'pack':
			namespace[name].pack(namespace[args])
for name in sorted(namespace.keys()):
	print(f'{name} {namespace[name].x} {namespace[name].y}')
