from bisect import bisect_left, bisect_right

def solve(a, b, c, d):
	return sum((bisect_right(c, v) for v in b)) - sum((bisect_left(d, u) for u in a))
((a, b), (c, d)) = (zip(*(map(int, input().split()) for _ in range(k))) for k in map(int, input().split()))
print(solve(a, b, sorted(c), sorted(d)))
