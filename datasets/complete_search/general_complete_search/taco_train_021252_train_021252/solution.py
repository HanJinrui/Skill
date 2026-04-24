for _ in range(int(input())):
	n = int(input())
	m = [int(i) for i in input().split()]
	x = [sum([int(i) for i in str(m[i] * m[j]).strip()]) for i in range(n) for j in range(i + 1, n)]
	print(max(x))
