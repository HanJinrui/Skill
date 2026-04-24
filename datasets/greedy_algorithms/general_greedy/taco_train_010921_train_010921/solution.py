for _ in range(int(input())):
	(s, t) = input().split()
	check = ''
	for ch in s[::-1]:
		if ch in t and check.count(ch) < t.count(ch):
			check += ch
	if check == t[::-1]:
		print('YES')
	else:
		print('NO')
