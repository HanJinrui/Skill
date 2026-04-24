def mgcd(a, b):
	while b > 0:
		(a, b) = (b, a % b)
	return a

def reduction(arr, mdl):
	totred = 0
	for e in range(len(arr)):
		(red, arr[e]) = divmod(arr[e], mdl)
		totred += red
	return totred

def submins(arr, red, g, mdl):
	submin = [mdl + 1] * g
	rx = red % g
	submin[rx] = arr[-1] - arr[0]
	for ix in range(1, len(arr)):
		thmin = mdl + arr[ix - 1] - arr[ix]
		rx = rx - 1 if rx > 0 else g - 1
		if thmin < submin[rx]:
			submin[rx] = thmin
	return submin
(n, m, x) = map(int, input().split())
z = input().strip().split()
s = list(map(int, z[:n]))
z = input().strip().split()
t = list(map(int, z[:m]))
g = mgcd(n, m)
sred = reduction(s, x)
tred = reduction(t, x)
s.sort()
t.sort()
smin = submins(s, sred, g, x)
tmin = submins(t, tred, g, x)
ans = smin[0] + tmin[0]
for (sm, tm) in zip(smin, tmin):
	if sm + tm < ans:
		ans = sm + tm
print(ans)
