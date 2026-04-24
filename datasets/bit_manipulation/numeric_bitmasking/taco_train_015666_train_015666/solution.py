for _ in range(int(input())):
	n = int(input())
	s = input()
	ans = 'NO'
	if s.count('1') == s.count('0') or s.count('0') % 2 == 0 or s.count('1') % 2 == 0:
		ans = 'YES'
	print(ans)
