s = input()
k = int(input())
a = []
for x in set(s):
	a.append([s.count(x), x])
a.sort()
for z in a:
	if z[0] > k:
		break
	k -= z[0]
	s = s.replace(z[1], '')
print(len(set(s)))
print(s)
