A = list(input())
S = list(input())
S.sort()
for (i, v) in enumerate(A):
	if S == []:
		break
	if v < S[-1]:
		A[i] = S[-1]
		S.pop()
print(''.join(A))
