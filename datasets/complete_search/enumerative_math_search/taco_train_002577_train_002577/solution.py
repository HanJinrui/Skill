s = list()

def rec(x):
	if x > 100000000000:
		return
	s.append(x)
	rec(x * 10 + 4)
	rec(x * 10 + 7)

def f(l1, r1, l2, r2):
	l1 = max(l1, l2)
	r1 = min(r1, r2)
	return max(r1 - l1 + 1, 0)

def main():
	rec(0)
	s.sort()
	args = input().split()
	(pl, pr, vl, vr, k) = (int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]))
	ans = 0
	i = 1
	while i + k < len(s):
		l1 = s[i - 1] + 1
		r1 = s[i]
		l2 = s[i + k - 1]
		r2 = s[i + k] - 1
		a = f(l1, r1, vl, vr) * f(l2, r2, pl, pr)
		b = f(l1, r1, pl, pr) * f(l2, r2, vl, vr)
		ans += a + b
		if k == 1 and a > 0 and (b > 0):
			ans -= 1
		i += 1
	all = (pr - pl + 1) * (vr - vl + 1)
	print(1.0 * ans / all)
main()
