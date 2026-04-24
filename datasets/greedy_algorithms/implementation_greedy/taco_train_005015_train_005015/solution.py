n = int(input())
c = []
k = 0
p = 1000000000000
for v in input().split()[::-1]:
	p = max(0, min(p - 1, int(v)))
	k += p
print(k)
