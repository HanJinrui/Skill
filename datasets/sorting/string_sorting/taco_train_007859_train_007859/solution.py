a = set(map(int, input().split(',')))
l = [x for x in a]
l.sort()
ans = ''
for i in l:
	if i - 1 not in l:
		ans += ',' + str(i)
	elif i + 1 not in l:
		ans += '-' + str(i)
print(ans[1:])
