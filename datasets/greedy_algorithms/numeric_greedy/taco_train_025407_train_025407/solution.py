I = lambda : map(int, input().split())
(x, k) = I()
R = [0, x]
for _ in range(k):
	(_, *r) = I()
	R += r
R.sort()
max_ = min_ = 0
for i in range(len(R) - 1):
	min_ += (R[i + 1] - R[i]) // 2
	max_ += R[i + 1] - R[i] - 1
print(min_, max_)
