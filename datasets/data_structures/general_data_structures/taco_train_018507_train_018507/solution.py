for t in range(int(input())):
	n = int(input())
	N = list(map(int, input().split()))
	m = [m for m in N if m < 1000]
	print(n - len(m))
