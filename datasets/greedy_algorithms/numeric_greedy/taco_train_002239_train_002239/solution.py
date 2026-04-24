n = int(input())
qq = 0
for i in range(n):
	(h, m) = list(map(int, input().split()))
	k = 1
	r = 4
	while m > r:
		k += 1
		r *= 4
	qq = max(qq, h + k)
print(qq)
