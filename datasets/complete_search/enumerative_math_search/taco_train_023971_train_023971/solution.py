def f(arr):
	val = 0
	for x in arr:
		val ^= x
	return val

def solve(l, r, k):
	ret = [l]
	if k >= 2:
		cand = [l, l + 1]
		if f(cand) < f(ret):
			ret = cand
		if l + 2 <= r:
			cand = [l + 1, l + 2]
			if f(cand) < f(ret):
				ret = cand
	if k >= 3:
		x = 1
		while x <= l:
			x *= 2
		if x + x // 2 <= r:
			ret = [x - 1, x + x // 2, x + x // 2 - 1]
	if k >= 4:
		cand = [l, l + 1, l + 2, l + 3]
		if f(cand) < f(ret):
			ret = cand
		if l + 4 <= r:
			cand = [l + 1, l + 2, l + 3, l + 4]
			if f(cand) < f(ret):
				ret = cand
	return ret
(l, r, k) = map(int, input().split())
ans = solve(l, r, k)
print(f(ans))
print(len(ans))
print(' '.join(map(str, ans)))
