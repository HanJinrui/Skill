s = input()
ans = []
count = 0
last_pos = s.rfind('#')
n = len(s)
for i in range(n):
	if s[i] == '(':
		count += 1
	elif s[i] == ')':
		count -= 1
	elif s[i] == '#' and i == last_pos:
		num = max(1, s.count('(') * 2 - len(s) + 1)
		count -= num
		ans.append(num)
	else:
		count -= 1
		ans.append(1)
	if count < 0:
		print(-1)
		exit(0)
for t in ans:
	print(t)
