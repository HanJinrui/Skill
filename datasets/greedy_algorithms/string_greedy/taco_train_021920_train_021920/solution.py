for _ in range(int(input())):
	n = int(input())
	ans = 'NO'
	set1 = set()
	set2 = set()
	for i in range(n):
		s = input()
		ss = s[::-1]
		if s == ss or s in set2 or s in set1 or (s[1:] in set1):
			ans = 'YES'
		set1.add(ss)
		if len(ss) == 3:
			set2.add(ss[1:])
	print(ans)
