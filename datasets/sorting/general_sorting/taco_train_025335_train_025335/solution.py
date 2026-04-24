for _ in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	l.sort(reverse=True)
	if l[-2] - l[-3] == 2 * (l[-1] - l[-2]) or 2 * (l[-2] - l[-3]) == l[-1] - l[-2]:
		print('Yes')
	else:
		print('No')
