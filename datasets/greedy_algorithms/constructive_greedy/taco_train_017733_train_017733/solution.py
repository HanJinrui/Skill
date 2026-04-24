for _ in range(int(input())):
	n = int(input())
	s = input()
	sort_s = ''.join(sorted(s))
	j = 0
	ans = ['0'] * n
	c1 = ''
	c2 = ''
	for i in range(n):
		if s[i] == sort_s[j]:
			ans[i] = '1'
			j += 1
			c1 += s[i]
		else:
			ans[i] = '2'
			c2 += s[i]
	if c1 + c2 == ''.join(sort_s):
		print(''.join(ans))
	else:
		print('-')
