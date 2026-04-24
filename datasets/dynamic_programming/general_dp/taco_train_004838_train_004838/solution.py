from functools import lru_cache
import sys
sys.setrecursionlimit(3000)
input()
a = input().split()
b = input().split()

@lru_cache(None)
def get(i, j):
	if i == len(a) or j == len(b):
		return []
	if a[i] == b[j]:
		return get(i + 1, j + 1) + [a[i]]
	q = get(i + 1, j)
	w = get(i, j + 1)
	if len(q) > len(w):
		return q
	return w
print(' '.join(get(0, 0)[::-1]))
