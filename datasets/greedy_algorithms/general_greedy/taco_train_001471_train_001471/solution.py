c = ans = 0
for i in input():
	if i == '(':
		c += 1
	elif c > 0:
		ans += 2
		c -= 1
print(ans)
