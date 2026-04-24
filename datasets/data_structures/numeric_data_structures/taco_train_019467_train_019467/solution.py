t = int(input())
for i in range(t):
	(s, a, b, c) = map(int, input().split())
	if a <= s * c / 100 + s <= b:
		print('Yes')
	else:
		print('No')
