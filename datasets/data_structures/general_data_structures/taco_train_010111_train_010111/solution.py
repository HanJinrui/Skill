N = int(input())
S = {}
for _ in range(N):
	s = input()
	ss = float(input())
	if ss not in S:
		S[ss] = []
	S[ss].append(s)
ss = sorted(S)
for s in sorted(S[ss[1]]):
	print(s)
