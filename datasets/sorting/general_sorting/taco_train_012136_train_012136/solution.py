from bisect import bisect as bs
from itertools import accumulate as ac
rd = lambda : map(int, input().split())
(n, q) = rd()
(A, k) = (rd(), rd())
a = list(ac(A))
wtf = 0
for i in range(q):
	wtf += next(k)
	j = bs(a, wtf)
	if j == n:
		wtf = 0
		j = 0
	print(n - j)
