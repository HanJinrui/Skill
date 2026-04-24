for i in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	s1 = 0
	s2 = 0
	ans = 'YES'
	for i in range(n - 1):
		s1 += l[i]
		s2 += n - i
		if s1 == s2:
			ans = 'NO'
			break
	print(ans)
