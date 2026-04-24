from statistics import mode
for _ in range(int(input())):
	N = int(input())
	S = input()
	print(N - S.count(mode(S)))
