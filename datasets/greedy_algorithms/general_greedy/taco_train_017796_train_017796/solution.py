input()
a = (*map(int, input().split()),)
b = (a[0], *(x * (a[0] >= 2 * x) for x in a[1:]))
if 2 * sum(b) <= sum(a):
	b = ()
print(sum(map(bool, b)), *(i for (i, x) in enumerate(b, 1) if x))
