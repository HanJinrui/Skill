from sys import *
from bisect import *
from collections import *
p = list(map(int, stdin.read().split()))
(n, k) = (p[0], p[1])
(s, d) = ([], Counter(p[2:2 + k]))
t = sorted((q for q in d if d[q] == 1))

def sub(q):
	if d[q] == 1:
		t.pop(bisect(t, q) - 1)

def add(q):
	if d[q] == 1:
		insort(t, q)

def get():
	s.append(str(t[-1]) if t else 'Nothing')
get()
for (a, b) in zip(p[2:], p[2 + k:]):
	if a != b:
		(sub(a), sub(b))
		d[b] += 1
		d[a] -= 1
		(add(a), add(b))
	get()
print('\n'.join(s))
