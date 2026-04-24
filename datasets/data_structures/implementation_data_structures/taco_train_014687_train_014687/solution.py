import re
(a, ans) = ([], 0)
for x in re.split('[:,]', input()):
	dl = x.count('.')
	if dl == 0:
		ans += a.count(x)
		a += [x]
	else:
		x = x[:-dl]
		ans += a.count(x)
		a += [x]
		a = a[:-dl]
print(ans)
