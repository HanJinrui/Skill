from collections import Counter
for _ in range(int(input())):
	n = int(input())
	a = Counter(input().split()).most_common(2)
	print('YES' if len(a) == 1 or a[0][1] > a[1][1] else 'NO')
