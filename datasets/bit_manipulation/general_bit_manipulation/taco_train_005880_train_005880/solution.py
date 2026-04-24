NUM_BITS = 8

def rev0(k):
	res = 0
	for i in range(NUM_BITS):
		res <<= 1
		res += k & 1
		k >>= 1
	return res
string_arr = [''.join(('ab'[k >> i & 1] for i in range(NUM_BITS))) for k in range(2 ** NUM_BITS)]
masks_arr = [(1 << i) - 1 for i in range(NUM_BITS + 1)]
bincnt_arr = bytes((sum((k >> i & 1 for i in range(NUM_BITS))) for k in range(2 ** NUM_BITS)))
rev_arr = bytes((rev0(k) for k in range(2 ** NUM_BITS)))
from collections import namedtuple
Seq = namedtuple('Seq', 'arr len shift')

def seq_str(self):
	lines = (f'Seq of {self.len} bits on {len(self.arr)} bytes, shift={self.shift}', ' '.join((string_arr[x] for x in self.arr))[self.shift:self.len + len(self.arr) - 1])
	return '\n'.join(lines)
Seq.__str__ = seq_str

def as_seq(string):

	def it():
		v = i = 0
		for c in string:
			if c == 'b':
				v |= 1 << i
			i += 1
			if i == NUM_BITS:
				yield v
				v = i = 0
		if i > 0:
			yield v
	return Seq(bytearray(it()), len(string), 0)

def as_string(s, l, r):
	l += s.shift
	r += s.shift
	(a0, a1) = (l >> 3, l & 7)
	b0 = r - 1
	b0 = (b0 >> 3) + (b0 & 7 > 0)
	return ''.join((string_arr[x] for x in s.arr[a0:b0 + 1]))[a1:a1 + r - l]

def hamming(s1, s2):
	s1 = set_shift(s1, 0)
	s2 = set_shift(s2, 0)
	len0 = len(s1.arr)
	i1 = int.from_bytes(s1.arr, 'little')
	i2 = int.from_bytes(s2.arr, 'little')
	return sum((i1 ^ i2).to_bytes(len0, 'little').translate(bincnt_arr))

def first_bits(b, i):
	return b & masks_arr[i]

def sub_seq(seq, l, r):
	len0 = r - l
	if len0 > 0:
		l += seq.shift
		r += seq.shift
		r -= 1
		(r0, r1) = (r >> 3, r & 7)
		(l0, l1) = (l >> 3, l & 7)
		arr = seq.arr
		if r0 == l0:
			b = bytes([arr[l0] & ~masks_arr[l1] & masks_arr[r1 + 1]])
		else:
			b = bytes([arr[l0] & ~masks_arr[l1]]) + arr[l0 + 1:r0] + bytes([arr[r0] & masks_arr[r1 + 1]])
		return Seq(b, l1 + len0, l1)
	else:
		return Seq(bytes(), 0, 0)

def set_shift(seq, shift=0):
	d_shift = seq.shift - shift
	if d_shift > 0:
		len0 = seq.len - d_shift
		lenb = (len0 >> 3) + (len0 & 7 > 0)
		b = (int.from_bytes(seq.arr, 'little') >> d_shift).to_bytes(lenb, 'little')
		seq = Seq(b, len0, shift)
	elif d_shift < 0:
		len0 = seq.len - d_shift
		lenb = (len0 >> 3) + (len0 & 7 > 0)
		b = (int.from_bytes(seq.arr, 'little') << -d_shift).to_bytes(lenb, 'little')
		seq = Seq(b, len0, shift)
	return seq

def seq_getitem(self, s):
	len0 = self.len
	l = s.start if s.start is not None else 0
	r = s.stop if s.stop is not None else len0 - self.shift
	if l < 0:
		l += len0
	if r < 0:
		r += len0
	return sub_seq(self, l, r)
Seq.__getitem__ = seq_getitem

def add_seq(self, other):
	if other.len == 0:
		return self
	if self.len == 0:
		return other
	r = self.len
	(r0, r1) = (r >> 3, r & 7)
	other = set_shift(other, r1)
	if r1 == 0:
		b = self.arr + other.arr
	else:
		b0 = self.arr[:-1]
		b1 = bytes([self.arr[-1] | other.arr[0]])
		b2 = other.arr[1:]
		b = b0 + b1 + b2
	return Seq(b, self.len + other.len - other.shift, self.shift)
Seq.__add__ = add_seq

def rev_seq(self):
	r = (len(self.arr) << 3) - self.len
	b = self.arr.translate(rev_arr)[::-1]
	return Seq(b, self.len - self.shift + r, r)

def zeros(n):
	arr_len = (n >> 3) + (n & 7 > 0)
	return Seq(bytes((0 for _ in range(arr_len))), n, 0)

def ones(n):
	arr_len = (n >> 3) + (n & 7 > 0)
	return Seq(bytes((255 for _ in range(arr_len))), n, 0)

def C(s, l, r, ch):
	(l, r) = (int(l) - 1, int(r))
	t = zero_seq if ch == 'a' else one_seq
	return s[:l] + t[:r - l] + s[r:]

def S(s, l1, r1, l2, r2):
	(l1, r1, l2, r2) = (int(l1) - 1, int(r1), int(l2) - 1, int(r2))
	return s[:l1] + s[l2:r2] + s[r1:l2] + s[l1:r1] + s[r2:]

def R(s, l, r):
	(l, r) = (int(l) - 1, int(r))
	return s[:l] + rev_seq(s[l:r]) + s[r:]

def W(s, l, r):
	(l, r) = (int(l) - 1, int(r))
	result.append(as_string(s, l, r))
	return s

def H(s, l1, l2, len0):
	(l1, l2, len0) = (int(l1) - 1, int(l2) - 1, int(len0))
	result.append(hamming(s[l1:l1 + len0], s[l2:l2 + len0]))
	return s
handlers = {f.__name__: f for f in [S, C, R, W, H]}
n = int(input())
s = input()
s = as_seq(s)
zero_seq = zeros(n)
one_seq = ones(n)
m = int(input())
queries = [input().split() for _ in range(m)]
result = []
for q in queries:
	s = handlers[q[0]](s, *q[1:])
print(*result, sep='\n')
