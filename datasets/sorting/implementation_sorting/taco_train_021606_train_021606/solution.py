t = int(input())
for i in range(t):
	(n, k) = map(int, input().split())
	l = list(map(int, input().split()))
	for j in range(k):
		l[j::k] = sorted(l[j::k])
	print('yes' if l == sorted(l) else 'no')
