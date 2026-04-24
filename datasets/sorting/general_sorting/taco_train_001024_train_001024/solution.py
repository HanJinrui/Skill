_ = int(input())
while _:
	_ -= 1
	n = int(input())
	l = list(map(int, input().split()))
	s = input()
	nl = sorted(l)
	if l == nl:
		print(0)
	elif 'N' not in s or 'S' not in s:
		print(-1)
	elif s[0] != s[-1]:
		print(1)
	else:
		fn = s.index('N')
		fs = s.index('S')
		ln = n - s[::-1].index('N')
		ls = n - s[::-1].index('S')
		if l[:fn] + sorted(l[fn:ls]) + l[ls:] == nl or l[:fs] + sorted(l[fs:ln]) + l[ln:] == nl:
			print(1)
		else:
			print(2)
