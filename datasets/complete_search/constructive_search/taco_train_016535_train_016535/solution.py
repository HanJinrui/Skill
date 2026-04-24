input()
a = sorted(map(int, input().split()))
b = [a.pop(0)]
c = a[-1] > 0 and [a.pop()] or [a.pop(0), a.pop(0)]
for l in (b, c, a):
	print(len(l), *l)
