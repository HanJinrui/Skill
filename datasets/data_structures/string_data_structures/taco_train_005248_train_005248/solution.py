def mini(s, t):
	l = len(s)
	ops = 0
	for i in range(l - 1):
		if s[i] != t[i]:
			s[i] = 1 - s[i]
			s[i + 1] = 1 - s[i + 1]
			ops += 1
	return ops
Test = int(input())
for test in range(Test):
	temp = input().split()
	ops = []
	(n, m) = (int(temp[0]), int(temp[1]))
	S_str = input()
	T_str = input()
	s = list(S_str)
	t = list(T_str)
	S = [int(x) for x in s]
	T = [int(x) for x in t]
	if len(S) > len(T):
		pass
	else:
		for i in range(len(T) - len(S) + 1):
			T_temp = T[i:i + len(S)]
			if (sum(T_temp) - sum(S)) % 2 != 0:
				if len(S) == len(T):
					pass
				else:
					temp = [1 + mini([1 - S[0]] + S[1:], T_temp), 1 + mini(S[:-1] + [1 - S[-1]], T_temp)]
					ops = ops + temp
			else:
				ops.append(mini(S[:], T_temp))
				if len(T) > len(S) + 1:
					ops.append(2 + mini([1 - S[0]] + S[1:-1] + [1 - S[-1]], T_temp))
	if ops == []:
		print('-1')
	else:
		ans = min(ops) + len(T) - len(S)
		print(ans)
