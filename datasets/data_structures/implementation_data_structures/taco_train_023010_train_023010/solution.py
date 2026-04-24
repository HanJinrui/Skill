for _ in range(int(input())):
	N = int(input())
	A = [x for x in input().split()]
	K = int(input())
	B = set([x for x in input().split()])
	print(*[a for a in A if a not in B])
