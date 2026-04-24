T = int(input())
for t in range(T):
	N = int(input()) + 2
	s = '1' + input() + '1'
	A = [-10000000000] + [int(x) for x in input().split()] + [10000000000]
	ss = 0
	mm = 0
	ans = 0
	for i in range(1, N):
		ss += A[i] - A[i - 1]
		mm = max(mm, A[i] - A[i - 1])
		if s[i] == '1':
			ans += ss - mm
			ss = 0
			mm = 0
	print(ans)
