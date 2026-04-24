n = int(input())
p = list(map(int, input().split()))
x = list(map(int, input().split()))
m = int(input())
y = list(map(int, input().split()))
r = list(map(int, input().split()))
cl = sorted([(c - d, c + d) for (c, d) in zip(y, r)])
tn = sorted(list(zip(x, p)))
from collections import Counter
q = Counter()
alr = 0
(i, k) = (0, 0)
while i < len(cl) and k < len(tn):
	(beg, end) = cl[i]
	pos = tn[k][0]
	if beg > pos:
		alr += tn[k][1]
		k += 1
	elif end < pos:
		i += 1
	else:
		cur = cl[i]
		while i + 1 < len(cl) and cl[i + 1][1] < pos:
			i += 1
		cl[i] = cur
		if i + 1 == len(cl) or cl[i + 1][0] > pos:
			q[cur] += tn[k][1]
		k += 1
while k < len(tn):
	alr += tn[k][1]
	k += 1
print(alr + (q.most_common()[0][1] if q else 0))
