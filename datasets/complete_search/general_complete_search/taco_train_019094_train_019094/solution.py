for _ in range(int(input())):
	(a, o) = input().split()
	su = 0
	for i in range(int(a)):
		s = input().split()
		if s[0] == 'CONTEST_WON':
			su += 300 + max([0, 20 - int(s[1])])
		elif s[0] == 'TOP_CONTRIBUTOR':
			su += 300
		elif s[0] == 'BUG_FOUND':
			su += int(s[1])
		else:
			su += 50
	if o == 'INDIAN':
		print(su // 200)
	else:
		print(su // 400)
