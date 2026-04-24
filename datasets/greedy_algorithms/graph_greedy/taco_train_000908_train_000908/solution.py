alph = 'qwertyuiopasdfghjklzxcvbnm'
for _ in range(int(input())):
	s = input()
	ans = s[0]
	t = 0
	for i in range(1, len(s)):
		if s[i] not in ans:
			if s[i - 1] == ans[-1]:
				ans += s[i]
			elif s[i - 1] == ans[0]:
				ans = s[i] + ans
			else:
				t = 1
				break
		elif abs(ans.find(s[i]) - ans.find(s[i - 1])) > 1:
			t = 1
			break
	if t:
		print('NO')
	else:
		print('YES')
		print(ans + ''.join([i for i in alph if i not in ans]))
