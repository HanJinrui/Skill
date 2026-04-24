for i in range(int(input())):
	l = list(map(int, input().split()))
	s = str(input())
	for i in s:
		l[ord(i) - 97] = 0
	print(sum(l))
