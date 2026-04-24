n = int(input())
widgets = {}

class Widget:

	def __init__(self, w, h):
		self.w = w
		self.h = h

	def calc_size(self):
		return (self.w, self.h)

class Box:

	def __init__(self, direction):
		self.dir = direction
		self.packed = []
		self.border = 0
		self.spacing = 0
		self.size = None

	def calc_size(self):
		if self.size is not None:
			return self.size
		if not len(self.packed):
			self.size = (0, 0)
			return self.size
		child_sizes = []
		for kid in self.packed:
			child_sizes.append(kid.calc_size())
		s = 0
		for kid in child_sizes:
			s += kid[self.dir == 'V']
		s += self.spacing * max(0, len(self.packed) - 1)
		mx = 0
		for kid in child_sizes:
			mx = max(mx, kid[self.dir == 'H'])
		self.size = (mx + 2 * self.border, s + 2 * self.border)
		if self.dir == 'H':
			self.size = (self.size[1], self.size[0])
		return self.size
for _ in range(n):
	s = input().strip()
	spacespl = s.split(' ')
	if len(spacespl) > 1:
		(cmd, rest) = spacespl
		if cmd == 'Widget':
			(name, rest) = rest.split('(')
			(w, h) = map(int, rest[:-1].split(','))
			widgets[name] = Widget(w, h)
		elif cmd == 'HBox':
			widgets[rest] = Box('H')
		elif cmd == 'VBox':
			widgets[rest] = Box('V')
	else:
		(name1, rest) = s.split('.')
		(method, args) = rest[:-1].split('(')
		if method == 'pack':
			widgets[name1].packed.append(widgets[args])
		elif method == 'set_border':
			widgets[name1].border = int(args)
		elif method == 'set_spacing':
			widgets[name1].spacing = int(args)
for (name, thing) in sorted(widgets.items()):
	print(name, *thing.calc_size())
