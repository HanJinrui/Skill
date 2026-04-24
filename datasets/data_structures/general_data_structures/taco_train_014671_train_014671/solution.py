for _ in range(int(input())):
	s = input().strip()
	k = int(input())
	sm = alters = 0
	prev = None
	for i in s:
		if i != prev:
			alters += 1
		prev = i
		if i == '(':
			sm += 1
		else:
			sm -= 1
		if sm < 0:
			break
	if sm != 0:
		if k != 1:
			print(-1)
		else:
			print(s)
	elif alters < k:
		print(-1)
	else:
		(lo, hi) = (0, alters)
		prev = None
		for i in range(len(s)):
			if prev == '(' and s[i] == ')':
				lo += 1
			elif prev == ')' and s[i] == '(':
				hi -= 1
			prev = s[i]
			if lo == k or hi == k:
				print(s[:i] + s[i + 1:])
				break
