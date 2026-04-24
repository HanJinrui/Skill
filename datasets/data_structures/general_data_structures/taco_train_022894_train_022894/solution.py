from bisect import bisect
n = int(input())
a = [n + 1, *map(int, input().split())]
ans = 0
inc = []
dec = [0]
for i in range(1, n + 1):
	while a[dec[-1]] < a[i]:
		dec.pop()
	x = dec[-1]
	dec.append(i)
	k = bisect(inc, x)
	ans += 1 + len(inc) - k
	while inc and a[inc[-1]] > a[i]:
		inc.pop()
	inc.append(i)
print(ans)
