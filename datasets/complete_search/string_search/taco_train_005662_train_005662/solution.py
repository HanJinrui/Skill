ans = []
s = 'abcdefghijklmnopqrstuvwxyz'
for i in s:
	ans.append(i)
	for j in s:
		ans += [i + j] + [i + j + k for k in s]
ans.sort(key=len)
for t in range(int(input())):
	n = int(input())
	s = input()
	for i in ans:
		if s.find(i) == -1:
			print(i)
			break
