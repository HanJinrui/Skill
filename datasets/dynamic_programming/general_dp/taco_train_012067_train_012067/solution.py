a = input()
if 'w' in a or 'm' in a:
	print(0)
	exit()
p = 'TKD'
x = [0, 1]
mod = pow(10, 9) + 7
for i in a:
	if i == p and i in 'nu':
		x += [(x[-1] + x[-2]) % mod]
	else:
		x += [x[-1] % mod]
	p = i
print(x[-1])
