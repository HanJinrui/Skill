for _ in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	m = max(l)
	i = l.index(m)
	s = 'NO'
	if l[:i] == sorted(l[:i]) and l[i:n] == sorted(l[i:n])[::-1]:
		s = 'YES'
	print(s)
