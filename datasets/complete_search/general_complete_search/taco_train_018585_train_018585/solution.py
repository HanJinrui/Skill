from bisect import bisect_left as bisect
(N, ar) = (int(input()), [int(x) for x in input().split()])
(Q, qr) = (int(input()), [int(x) for x in input().split()])
ar = sorted(ar)
Sc = [0]
for x in ar:
	Sc.append(x + Sc[-1])
q = 0
for x in qr:
	q += x
	n = bisect(ar, -q)
	print(Sc[-1] - 2 * Sc[n] + q * (N - 2 * n))
