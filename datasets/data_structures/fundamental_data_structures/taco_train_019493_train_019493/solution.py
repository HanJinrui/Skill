def check(s):
	if len(s)<26:
		return 'No'
	l=[s.count(i) for i in set(s)]
	c=s.count('a')
	if c*len(set(s))==sum(l):
		return 'Yes'
	return 'No'
	
	
for _ in range(eval(input())):
	s=input()
	print((check(s)))
