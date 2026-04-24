T = int(input())
for _ in range(T):
	N = int(input())
	S = input()
	P = input()
	if P.count('1') in [len(P), 0]:
		print(['NO', 'YES'][S == P])
	else:
		print('YES')
