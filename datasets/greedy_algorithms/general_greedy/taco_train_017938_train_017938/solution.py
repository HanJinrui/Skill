from heapq import *
k = d = 0
(s, h) = ([], [])
for (i, q) in enumerate(input()):
	if q == '?':
		q = ')'
		(x, y) = map(int, input().split())
		d += y
		heappush(h, (x - y, i))
	s.append(q)
	if q == '(':
		k += 1
	elif k:
		k -= 1
	elif h:
		k = 1
		(x, i) = heappop(h)
		d += x
		s[i] = '('
	else:
		k = 1
		break
print(-1) if k else print(d, ''.join(s))
