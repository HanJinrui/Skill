def restofs(s, k):
	lst = []
	for i in s:
		while len(lst) > 0 and k != 0 and (lst[-1] > i):
			lst.pop()
			k -= 1
		lst.append(i)
	while len(lst) > 0 and k != 0:
		lst.pop()
		k -= 1
	return ''.join(lst)
for __ in range(int(input())):
	s = input()
	k = int(input())
	(i, x) = (0, s[0])
	for j in range(1, k + 1):
		if s[j] > '0' and s[j] < x:
			x = s[j]
			i = j
	print(x + restofs(s[i + 1:], k - i))
