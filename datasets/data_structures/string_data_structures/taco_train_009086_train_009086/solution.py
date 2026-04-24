for _ in range(int(input())):
	N = int(input())
	s = input()
	S = [*s]
	i = 0
	j = N - 1
	freeze = -1
	c = 0
	while i <= j:
		if S[i] != S[j]:
			if S[i + 1] == S[j] and freeze != i:
				(S[i], S[i + 1]) = (S[i + 1], S[i])
				freeze = i + 1
				c += 1
			elif S[j - 1] == S[i] and freeze != j:
				(S[j - 1], S[j]) = (S[j], S[j - 1])
				freeze = j - 1
				c += 1
			else:
				break
		i += 1
		j -= 1
	if S == S[::-1]:
		print('YES')
		print(c)
	else:
		print('NO')
