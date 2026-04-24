for _ in range(int(input())):
	N = int(input())
	S = str(input())
	l = -1
	for i in range(N):
		if S[i] != S[0]:
			l = i
			break
	if l == -1:
		print(0)
		continue
	p = 0
	for i in range(l, N):
		if S[i] == S[l]:
			p += 1
		else:
			break
	p = min(p, l)
	ans = 0
	x = 1
	for i in range(N - 1, l - 1, -1):
		if S[i] != S[i - p]:
			ans = (ans + x) % 1000000007
		x = x * 2 % 1000000007
	print(ans)
