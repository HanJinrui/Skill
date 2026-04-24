def solve():
	n = int(input())
	s = list(map(int, input().split()))
	a = []
	for x in s:
		z = x % 10
		if a.count(z) < 3:
			a.append(z)
	for i in range(len(a)):
		for j in range(i):
			for k in range(j):
				if (a[i] + a[j] + a[k]) % 10 == 3:
					return 'YES'
	return 'NO'
for _ in range(int(input())):
	print(solve())
