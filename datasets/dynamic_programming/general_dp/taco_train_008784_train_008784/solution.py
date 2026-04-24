n = int(input())
ar = list(map(int, input().split()))
m = int(input())
br = list(map(int, input().split()))
t = [0] * m
A = [[] for i in range(m)]
for i in range(n):
	c = 0
	p = -1
	for j in range(m):
		if ar[i] == br[j] and c + 1 > t[j]:
			t[j] = c + 1
			A[j] = (A[p] if p != -1 else []) + [ar[i]]
		if ar[i] > br[j] and c < t[j]:
			c = t[j]
			p = j
mx = max(t)
print(mx)
if mx > 0:
	ar = []
	for el in A:
		if len(el) > len(ar):
			ar = el
	print(*ar)
