def mi():
	return map(int, input().split())

def li():
	return list(mi())

def si():
	return str(input())

def ni():
	return int(input())
for t in range(int(input())):
	s = str(input())
	if s.count('1') == 1:
		print(-1)
		continue
	n = int(s, 2)
	mod = n % 3
	if mod == 0:
		print(0)
		continue
	a = []
	s = s[::-1]
	for i in range(len(s)):
		if i % 2 == 1 and s[i] == '1':
			a.append(2)
		else:
			a.append(int(s[i]))
	flag = False
	for i in range(len(a) - 1):
		if a[i] == 3 - mod and a[i + 1] == 0 or (a[i + 1] == 3 - mod and a[i] == 0):
			flag = True
	if flag:
		print(1)
	else:
		count = 0
		for i in range(len(a)):
			if a[i] == 0:
				if i > 0 and a[i - 1] == mod or (i < len(a) - 1 and a[i + 1] == mod):
					count += 1
		if count >= 2:
			print(2)
		elif '1100' in s or '0011' in s:
			print(3)
		else:
			print(-1)
