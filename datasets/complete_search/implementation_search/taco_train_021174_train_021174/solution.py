for _ in range(int(input())):
	k = int(input())
	s = list(input())
	if k == 2:
		for i in range(len(s)):
			if s[i] != '?':
				s[i % 2] = s[i]
				break
	bf = False
	for i in range(len(s)):
		nd = s[(i + 1) % len(s)]
		if s[i] != '?' and s[i] == nd:
			bf = True
			break
	if bf and len(s) > 1:
		ans = 'NO'
	else:
		for i in range(len(s)):
			if s[i] == '?':
				pd = s[i - 1]
				nd = s[(i + 1) % len(s)]
				for j in range(k):
					if str(j) != pd and str(j) != nd:
						s[i] = str(j)
						break
			if s[i] == '?':
				bf = True
				break
		if bf and len(s) > 1:
			ans = 'NO'
		else:
			ans = ''.join(s)
	print(ans)
