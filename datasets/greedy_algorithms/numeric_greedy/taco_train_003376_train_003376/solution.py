for _ in range(int(input())):
	__ = input()
	A = set(map(int, input().split()))
	B = set(map(int, input().split()))
	print(len(A.intersection(B)))
